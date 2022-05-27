#!/bin/env python3

import json
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdin"

with open(file, "r") as f:
    data = json.load(f)
    

for i in data:
    for j in data[i]:
        print(i, j, data[i][j])
