# /// script
# requires-python = ">=3.11,<3.14"
# dependencies = ["numpy"]
# ///
"""Onset detection on a take's audio: click sfx, chimes/dings, whooshes — the exact-time
event log of the take.

  afconvert -f WAVE -d LEI16@48000 -c 1 take.mov take.wav
  uv run audio_events.py take.wav <name> [beats.tsv]

beats.tsv (t_seconds<TAB>label, e.g. from clock_lint.py) labels each onset with its
nearest expected driver beat (press latency ~1.15s after until())."""
import numpy as np, wave, sys, os

WAV = sys.argv[1]
NAME = sys.argv[2] if len(sys.argv) > 2 else "take"
OUTDIR = "."

w = wave.open(WAV)
sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
w.close()

# short-time energy envelope (10ms hops) + spectral centroid for rough classing
hop = int(sr * 0.01); win = int(sr * 0.03)
n = (len(x) - win) // hop
env = np.empty(n); cent = np.empty(n)
freqs = np.fft.rfftfreq(win, 1/sr)
for i in range(n):
    seg = x[i*hop : i*hop+win]
    env[i] = np.sqrt((seg**2).mean())
    if i % 3 == 0:  # centroid every 30ms is plenty
        S = np.abs(np.fft.rfft(seg * np.hanning(win)))
        cent[i] = (S*freqs).sum() / (S.sum() + 1e-9)
    else:
        cent[i] = cent[i-1]
db = 20*np.log10(env + 1e-9)

# onsets: envelope rises >12dB over 60ms above a noise floor, min 250ms apart
floor = np.percentile(db, 20)
events = []
i = 6
while i < n:
    rise = db[i] - db[i-6]
    if db[i] > floor + 18 and rise > 12:
        t = i*hop/sr
        # measure duration above (peak-12dB)
        peak = db[i:i+40].max()
        j = i
        while j < n and db[j] > peak - 15: j += 1
        dur = (j-i)*hop/sr
        c = cent[i:i+12].mean()
        kind = ("click" if dur < 0.14 else
                "chime/ding" if c > 1400 and dur < 1.2 else
                "whoosh/other")
        events.append((t, dur, c, kind))
        i = j + 25
    else:
        i += 1

# expected sfx from the shot clock (t0=0): press ≈ until+1.15 for clicks
CLOCK = []
if len(sys.argv) > 3:
    for line in open(sys.argv[3]):                          # beats TSV: t_seconds<TAB>label
        parts = line.strip().split('\t')
        try: CLOCK.append((parts[1] if len(parts) > 1 else f"beat@{parts[0]}", float(parts[0]) + 1.15))
        except ValueError: continue
if not CLOCK:
    CLOCK = [("(no beats file given)", -999)]

with open(f"{OUTDIR}/audio-events-{NAME}.tsv", "w") as f:
    f.write("t_s\tdur_s\tcentroid_hz\tkind\tnearest_expected\n")
    for t, dur, c, kind in events:
        near = min(CLOCK, key=lambda e: abs(e[1]-t))
        tag = f"{near[0]} (Δ{t-near[1]:+.2f}s)" if abs(near[1]-t) < 1.6 else "-"
        f.write(f"{t:.2f}\t{dur:.2f}\t{c:.0f}\t{kind}\t{tag}\n")

print(f"{len(events)} audio events → audio-events-{NAME}.tsv")
for t, dur, c, kind in events:
    near = min(CLOCK, key=lambda e: abs(e[1]-t))
    tag = f"→ {near[0]} (Δ{t-near[1]:+.2f}s)" if abs(near[1]-t) < 1.6 else ""
    print(f"  {t:7.2f}s  {kind:<13} dur {dur:4.2f}s  cent {c:5.0f}Hz  {tag}")
