#!/usr/bin/env python3
"""Extract a dotted-path field. argv[1]=path, argv[2] or stdin=JSON."""
import sys, json

path = sys.argv[1] if len(sys.argv) > 1 else "user.name"
raw = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()
if not raw.strip():
    raw = '{"user": {"name": "Ada", "id": 1}}'

cur = json.loads(raw)
for part in path.split("."):
    if isinstance(cur, dict) and part in cur:
        cur = cur[part]
    else:
        sys.stderr.write("Path not found: %s\n" % path)
        sys.exit(1)
print(cur if isinstance(cur, str) else json.dumps(cur))