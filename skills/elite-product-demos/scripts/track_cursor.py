# /// script
# requires-python = ">=3.11,<3.14"
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""Track a demo driver's drawn cursor in a recorded take (self-bootstrapped template).

  uv run track_cursor.py take.mov --card-color '#132F1F' --beats beats.tsv \
      [--boot-at 10] [--outdir .] [--click-lag 1.15]

--card-color: the brand color of full-bleed hook/chapter cards (clock sync anchors).
--boot-at:    a moment when the cursor glides over a STATIC background (template bootstrap).
--beats:      TSV of driver-clock beats (t_seconds<TAB>label), e.g. from clock_lint.py.

1. Detect jade chapter cards → sync video time to the driver shot clock.
2. Bootstrap the cursor's real appearance by frame-differencing during the home-hover glides.
3. Track with masked TM_SQDIFF (numerically stable), local window + full-frame recovery.
Outputs: cursor-track-<name>.tsv, cursor-clicks-<name>.tsv (full-res video px)."""
import cv2, numpy as np, sys, os

def arg(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

VIDEO = sys.argv[1]
NAME = os.path.splitext(os.path.basename(VIDEO))[0]
OUTDIR = arg('--outdir', '.')
SCALE = 0.5
SAMPLE_MS = int(arg('--sample-ms', '100'))
_hex = arg('--card-color', '#132F1F').lstrip('#')          # full-bleed chapter/hook card color
JADE_BGR = np.array([int(_hex[4:6],16), int(_hex[2:4],16), int(_hex[0:2],16)])  # BGR
BOOT_START = float(arg('--boot-at', '10'))                  # a glide-over-static segment
BEATS = arg('--beats')                                      # TSV: t_seconds<TAB>label
CLICK_LAG = float(arg('--click-lag', '1.15'))               # until() -> press latency

def read_samples(video, times_s):
    """Grab half-res grayscale frames nearest the requested times (single pass)."""
    cap = cv2.VideoCapture(video)
    want = sorted(times_s); out = {}; wi = 0
    while wi < len(want):
        ok, frame = cap.read()
        if not ok: break
        t = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        if t >= want[wi]:
            small = cv2.resize(frame, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_AREA)
            out[want[wi]] = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
            wi += 1
    cap.release()
    return out

# ---- bootstrap template from the hover glides (10s..16s, static home behind) ----
boot_times = [round(BOOT_START + i*0.25, 2) for i in range(24)]
frames = read_samples(VIDEO, boot_times)
keys = sorted(frames)
tpl = msk = None
for a, b in zip(keys, keys[1:]):
    d = cv2.absdiff(frames[a], frames[b])
    _, thr = cv2.threshold(d, 25, 255, cv2.THRESH_BINARY)
    thr = cv2.dilate(thr, np.ones((5,5), np.uint8))
    cnts, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if not (14 <= w <= 90 and 14 <= h <= 90): continue
        pad = 3
        y0, y1 = max(0, y-pad), min(frames[b].shape[0], y+h+pad)
        x0, x1 = max(0, x-pad), min(frames[b].shape[1], x+w+pad)
        patch = frames[b][y0:y1, x0:x1]
        dark = (patch < 70).sum(); bright = (patch > 235).sum()
        if dark > 15 and bright > 40:                     # arrow rim + white body present
            tpl = patch.copy()
            m = ((patch < 80) | (patch > 228)).astype(np.uint8) * 255
            msk = cv2.dilate(m, np.ones((3,3), np.uint8))
            print(f"bootstrapped template {tpl.shape[1]}x{tpl.shape[0]} from t={b}s "
                  f"(dark {dark}, bright {bright}, mask {int(msk.sum()/255)})", flush=True)
            break
    if tpl is not None: break
if tpl is None: sys.exit("could not bootstrap cursor template from hover glides")
th, tw = tpl.shape
mask_n = max(1, int(msk.sum() / 255))

# ---- full pass: jade spans + tracking ----
cap = cv2.VideoCapture(VIDEO)
track, jade_spans = [], []
jade_open = last = None
next_t = 0.0

def match(gray, x0, y0, x1, y1):
    roi = gray[y0:y1, x0:x1]
    if roi.shape[0] <= th or roi.shape[1] <= tw: return None
    res = cv2.matchTemplate(roi, tpl, cv2.TM_SQDIFF, mask=msk)
    mv, _, ml, _ = cv2.minMaxLoc(res)
    err = float(np.sqrt(max(mv, 0) / mask_n))            # mean per-pixel error over the mask
    return err, ml[0]+x0, ml[1]+y0

while True:
    ok, frame = cap.read()
    if not ok: break
    t = cap.get(cv2.CAP_PROP_POS_MSEC)
    if t < next_t: continue
    next_t = t + SAMPLE_MS
    small = cv2.resize(frame, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_AREA)
    mean = small.reshape(-1,3).mean(axis=0)
    is_jade = np.abs(mean - JADE_BGR).sum() < 45
    if is_jade and jade_open is None: jade_open = t
    if not is_jade and jade_open is not None: jade_spans.append((jade_open, t)); jade_open = None
    if is_jade: continue
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    sh, sw = gray.shape
    hit = None
    if last is not None:
        lx, ly = last
        r = match(gray, max(0,lx-140), max(0,ly-140), min(sw,lx+140+tw), min(sh,ly+140+th))
        if r and r[0] < 26: hit = r
    if hit is None:
        r = match(gray, 0, 0, sw, sh)
        if r and r[0] < 20: hit = r
    if hit:
        err, mx, my = hit
        last = (mx, my)
        track.append((t, (mx+3)/SCALE, (my+3)/SCALE, err))   # +3 ≈ tip offset in patch

if jade_open is not None: jade_spans.append((jade_open, 999999))
cap.release()

with open(f"{OUTDIR}/cursor-track-{NAME}.tsv", "w") as f:
    f.write("t_ms\tx\ty\terr\n")
    for t, x, y, e in track: f.write(f"{t:.0f}\t{x:.0f}\t{y:.0f}\t{e:.1f}\n")

spans = [(round(a/1000,1), round(b/1000,1)) for a,b in jade_spans]
print(f"samples {len(track)}; jade spans {spans}", flush=True)
hook = next(((a,b) for a,b in jade_spans if b-a > 4000), None)
if hook and track:
    t0 = hook[0] / 1000.0
    CLICKS = []
    if BEATS:
        for line in open(BEATS):
            parts = line.strip().split('\t')
            try: CLICKS.append((parts[1] if len(parts) > 1 else f"beat@{parts[0]}", float(parts[0])))
            except ValueError: continue   # header
    ts = np.array([p[0] for p in track]) / 1000.0
    with open(f"{OUTDIR}/cursor-clicks-{NAME}.tsv", "w") as f:
        f.write("beat\tt_video_s\tx\ty\n")
        for name, sec in CLICKS:
            target = t0 + sec + CLICK_LAG
            w = np.where(np.abs(ts - target) < 1.4)[0]
            if len(w) < 2:
                print(f"  {name:<22} NO TRACK near {target:.1f}s", flush=True); continue
            best_i, best_v = None, 1e9
            for i in w[1:]:
                dx = abs(track[i][1]-track[i-1][1]) + abs(track[i][2]-track[i-1][2])
                if dx < best_v: best_v, best_i = dx, i
            t, x, y, e = track[best_i]
            f.write(f"{name}\t{t/1000:.2f}\t{x:.0f}\t{y:.0f}\n")
            print(f"  {name:<22} t={t/1000:7.2f}s  ({x:.0f},{y:.0f})  drift±{best_v:.0f}px", flush=True)
