#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit()

found = False
for i in range(1, len(sys.argv)):
    param = sys.argv[i]
    if not param.endswith("ism"):
        print(param + "ism")
        found = True

if not found:
    print("none")