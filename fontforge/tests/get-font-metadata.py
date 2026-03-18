#!/usr/bin/python3

import fontforge
import sys

if len(sys.argv) > 1:
    f = fontforge.open(sys.argv[1])
else:
    print("provide fontfile path as an argument")
    sys.exit(1)

if f.fullname:
    print("Fontname is {0}".format(f.fullname))
else:
    print("fontname not set")
if f.weight:
    print("Given font weight is {0}".format(f.weight))
else:
    print("Given font weight not set")
if f.version:
    print("Given font version is {0}".format(f.version))
else:
    print("Given font version not set")
if f.copyright:
    print("Given font Copyright text is => {0}".format(f.copyright))
else:
    print("Given font copyright information not set")

ver = fontforge.UnicodeNamesListVersion()
print("Libuninameslist version is : %s" % ver)

