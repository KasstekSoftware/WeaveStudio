#!/usr/bin/env python3
"""Pretty-print JSON. Input from argv[1], else stdin, else a built-in sample."""
import sys, json


def read_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    data = sys.stdin.read()
    return data if data.strip() else '{"b": 2, "a": 1, "items": [3, 1, 2]}'


try:
    obj = json.loads(read_input())
    print(json.dumps(obj, indent=2, sort_keys=True))
except ValueError as err:
    sys.stderr.write("Invalid JSON: %s\n" % err)
    sys.exit(1)