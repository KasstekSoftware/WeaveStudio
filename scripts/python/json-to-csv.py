#!/usr/bin/env python3
"""JSON array -> CSV. Input from argv[1], else stdin, else a built-in sample."""
import sys, csv, json, io


def read_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    data = sys.stdin.read()
    return data if data.strip() else '[{"name": "apples", "qty": 3}, {"name": "bread", "qty": 1}]'


rows = json.loads(read_input())
if not isinstance(rows, list) or not rows:
    sys.stderr.write("Expected a non-empty JSON array of objects\n")
    sys.exit(1)
out = io.StringIO()
writer = csv.DictWriter(out, fieldnames=list(rows[0].keys()))
writer.writeheader()
for row in rows:
    writer.writerow(row)
sys.stdout.write(out.getvalue())