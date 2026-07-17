#!/usr/bin/env python3
"""Lint a demo driver's shot clock and dump its beats.

  python3 clock_lint.py <driver.js> [--beats-out beats.tsv]

Checks every `until(N)` is monotonically increasing (a driver whose clock goes backwards
deadlocks a beat) and emits the beat list as TSV (name guessed from the nearest preceding
comment or finder string) for use by keyframe_zooms.py / audio_events.py.
"""
import re, sys

path = sys.argv[1]
beats_out = sys.argv[sys.argv.index('--beats-out') + 1] if '--beats-out' in sys.argv else None
src = open(path, encoding='utf-8').read()

rows, prev, bad = [], None, []
for m in re.finditer(r'until\(([\d.]+)\)', src):
    t = float(m.group(1))
    # label: nearest preceding // comment or quoted string on the same/next line
    tail = src[m.end():m.end()+200]
    q = re.search(r"'([^']{3,40})'|\"([^\"]{3,40})\"|/([^/]{3,40})/", tail)
    label = (q.group(1) or q.group(2) or q.group(3)) if q else ''
    rows.append((t, label.strip()))
    if prev is not None and t < prev:
        bad.append((prev, t))
    prev = t

for a, b in bad:
    print(f"ORDER VIOLATION: until({b}) after until({a})")
print(f"{len(rows)} beats, clock {'MONOTONIC' if not bad else 'BROKEN'}, last beat {rows[-1][0] if rows else '-'}s")
if beats_out:
    with open(beats_out, 'w') as f:
        f.write("t_seconds\tlabel\n")
        for t, label in rows:
            f.write(f"{t}\t{label}\n")
    print(f"wrote {beats_out}")
sys.exit(1 if bad else 0)
