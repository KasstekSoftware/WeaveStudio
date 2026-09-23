#!/usr/bin/env python3
"""CSV -> JSON. Input from argv[1], else stdin, else a built-in sample."""
import sys, csv, json, io


def read_input():
    if len(sys.argv) > 1:
        return sys.argv[1]
    data = sys.stdin.read()
    return data if data.strip() else "name,qty\napples,3\nbread,1"


rows = list(csv.DictReader(io.StringIO(read_input())))
print(json.dumps(rows, indent=2))