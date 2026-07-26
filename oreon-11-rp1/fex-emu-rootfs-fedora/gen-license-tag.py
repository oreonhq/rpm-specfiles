#!/usr/bin/env python3

import sys

licenses = []

EXCLUDE = set([
    "pubkey",
])

with open(sys.argv[1], "r") as f:
    for line in f:
        license = line.strip().split("|")[6]
        if license in EXCLUDE:
            continue

        if " " in license:
            licenses.append(f"({license})")
        else:
            licenses.append(license)

print(" AND ".join(sorted(set(licenses))))
