#!/usr/bin/python3
"""
Parse the package-lock.json to populate Provides for the spec

File: parse-deps.py

Copyright 2020 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import json


with open("package-lock.json", 'r') as f:
    lockfile = json.load(f)
    for depname, depdict in lockfile['dependencies'].items():
        if 'dev' not in depdict:
            print("Provides: bundled(nodejs-{}) = {}".format(
                depname, depdict['version']))
    # Generate package URLs to check license
    for depname, depdict in lockfile['dependencies'].items():
        if 'dev' not in depdict:
            print("https://www.npmjs.com/package/{}".format(depname))
