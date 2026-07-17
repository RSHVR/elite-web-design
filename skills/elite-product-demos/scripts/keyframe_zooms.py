#!/usr/bin/env python3
"""Compute editor keyframe rows for attention punch-ins (zooms) on a floating-window take.

  python3 keyframe_zooms.py --plan plan.json

plan.json:
{
  "canvas": [3676, 2160],          // project resolution
  "video":  [3456, 2032],          // take resolution
  "fps": 60,
  "base_scale": 0.88,              // resting window width, fraction of canvas (float look)
  "events": [
    { "name": "msg-banner",
      "t": 65.0,                   // DRIVER-CLOCK seconds (apply on the UNCUT take so
                                   // keyframes are clip-relative and survive later cuts)
      "focus_px": [3060, 360],     // attention target in VIDEO pixels (from cursor track,
                                   // or a fixed UI region like a banner corner)
      "zoom": 1.35,                // multiplier on base_scale
      "ease_in": 0.8, "hold": 2.3, "ease_out": 1.0 }
  ]
}

Output: JSON keyframe rows for `scale` and `position` (top-left, normalized canvas
coords, frames clip-relative) — the shape editor MCPs like Palmier's set_keyframes take.
Math: the focus point's canvas position at base framing is held fixed while scaling.
Warns when a zoomed frame fails to cover the canvas (background would peek through).
"""
import json, sys

plan = json.load(open(sys.argv[sys.argv.index('--plan') + 1]))
cw, ch = plan['canvas']; vw, vh = plan['video']; fps = plan.get('fps', 60)
sw0 = plan['base_scale']
sh0 = sw0 * (vh / vw) * (cw / ch)          # preserve the take's aspect on the canvas
tlx0, tly0 = (1 - sw0) / 2, (1 - sh0) / 2  # centered float

scale_rows = [[0, round(sw0, 5), round(sh0, 5)]]
pos_rows = [[0, round(tlx0, 5), round(tly0, 5)]]

for e in sorted(plan['events'], key=lambda e: e['t']):
    fx, fy = e['focus_px'][0] / vw, e['focus_px'][1] / vh
    z = e['zoom']
    w, h = sw0 * z, sh0 * z
    nx, ny = tlx0 + fx * sw0, tly0 + fy * sh0            # focus point at base framing
    tlx, tly = nx - fx * w, ny - fy * h                  # hold it fixed while zoomed
    if tlx > 0 or tly > 0 or tlx + w < 1 or tly + h < 1:
        cands = []
        for num, den in ((nx, fx * sw0), ((1 - nx), (1 - fx) * sw0),
                         (ny, fy * sh0), ((1 - ny), (1 - fy) * sh0)):
            if den > 1e-6: cands.append(num / den)
        zmin = max(cands) if cands else z
        print(f"WARN {e['name']}: zoomed frame does not cover canvas "
              f"(tl=({tlx:.3f},{tly:.3f}), br=({tlx+w:.3f},{tly+h:.3f})) — "
              f"minimum covering zoom for this focus is {zmin:.2f}", file=sys.stderr)
    f_anchor = round(e['t'] * fps)
    f_in = round((e['t'] + e['ease_in']) * fps)
    f_out_start = round((e['t'] + e['ease_in'] + e['hold']) * fps)
    f_out = round((e['t'] + e['ease_in'] + e['hold'] + e['ease_out']) * fps)
    scale_rows += [[f_anchor, round(sw0,5), round(sh0,5)], [f_in, round(w,5), round(h,5)],
                   [f_out_start, round(w,5), round(h,5)], [f_out, round(sw0,5), round(sh0,5)]]
    pos_rows += [[f_anchor, round(tlx0,5), round(tly0,5)], [f_in, round(tlx,5), round(tly,5)],
                 [f_out_start, round(tlx,5), round(tly,5)], [f_out, round(tlx0,5), round(tly0,5)]]

print(json.dumps({"scale": sorted(scale_rows), "position": sorted(pos_rows)}, indent=1))
