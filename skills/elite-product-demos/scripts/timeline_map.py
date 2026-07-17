#!/usr/bin/env python3
"""Map demo-driver (source) times to editor timeline frames through an edit's cuts.

  python3 timeline_map.py --pieces pieces.json --fps 60 --times 9.5,22,65

pieces.json describes the take's clips on the timeline (from the editor's timeline read):
  [{"start": 0, "end": 967, "trimStart": 0, "speed": 1}, ...]
start/end = timeline frames; trimStart = source offset in PROJECT frames; speed multiplier.
A time falling in a cut-out source range reports CUT and snaps to the next piece start.
Use AFTER the owner has cut the take (e.g. to lay VO); attention keyframes should have
been placed BEFORE cutting (clip-relative, they travel with the pieces).
"""
import json, sys

def arg(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

pieces = json.load(open(arg('--pieces')))
fps = float(arg('--fps', '60'))
times = [float(t) for t in arg('--times').split(',')]
pieces = sorted(pieces, key=lambda p: p['start'])

for s in times:
    sf = s * fps
    hit = None
    for p in pieces:
        speed = p.get('speed', 1) or 1
        t0 = p.get('trimStart', 0)
        span = (p['end'] - p['start']) * speed
        if t0 <= sf < t0 + span:
            hit = p['start'] + (sf - t0) / speed
            print(f"{s:8.2f}s -> frame {hit:7.1f}  (piece @{p['start']}, speed {speed})")
            break
    if hit is None:
        nxt = min((p for p in pieces if p.get('trimStart', 0) > sf), key=lambda p: p['trimStart'], default=None)
        snap = f"snap -> frame {nxt['start']}" if nxt else "past end"
        print(f"{s:8.2f}s -> CUT ({snap})")
