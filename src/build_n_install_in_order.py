#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: {} <ordered list path>".format(sys.argv[0]))
    exit(1)

file_path = sys.argv[1]

with open(file_path) as order_file:
    lines = order_file.read().split('\n')

filtered = []

for line in lines:
    if line != "" and line[0] != "#":
        filtered.append(line)

lines = filtered

for dirname in lines:
    if os.system("cd {} && makepkg --needed --noconfirm -sri".format(dirname)) != 0:
        exit(2)
