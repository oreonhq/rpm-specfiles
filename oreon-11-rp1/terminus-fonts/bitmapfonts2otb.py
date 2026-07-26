#!/usr/bin/python3

# This script is licensed under the GPL-3.0-or-later license.

# Automatically group the font files by family names and style names,
# and assume each bitmap font only contains one font face.
# This tool requires ftdump and fonttosfnt.

# Some changes by Hans Ulrich Niedermann and Antonio Larrosa.

# Written by Peng Wu as
# https://pwu.fedorapeople.org/fonts/convertbitmap/convertfont2.py
# Some changes by Hans Ulrich Niedermann.

import re
import sys
import subprocess

usage = '''
convertfont2.py [BITMAPFONTFILE]...
'''

fontnames = dict()

# get font family name and style name by ftdump
def get_fullname_height(fontname):
    output = subprocess.check_output(['ftdump', fontname])

    output = output.decode('utf8')
    # only contain one font face
    assert not 'Face number: 1' in output
    result = {}
    height = 0
    for row in output.split('\n'):
        # for family name and style name
        if ':' in row:
            key, value = row.split(': ')
            result[key.strip()] = value.strip()
        # for height
        if 'height' in row:
            match = re.search('height (\d+)', row)
            height = int(match.group(1))
            assert height > 0

    familyname, stylename = result['family'], result['style']
    if stylename == 'Regular':
        return (familyname, height)
    else:
        return (familyname + ' ' + stylename, height)


def generate_fonts():
    for (fullname, height), filenames in fontnames.items():
        outputfilename = fullname.replace(' ', '-') + '-' + str(height)  + '.otb'
        argv = 'fonttosfnt -b -c -g 2 -m 2 -o'.split(' ')
        argv.append(outputfilename)
        argv.extend(filenames)
        print(' '.join(argv))
        print(subprocess.check_output(argv).decode('utf8'))


if __name__ == '__main__':
    for bitmapfontname in sys.argv[1:]:
        (fullname, height) = get_fullname_height(bitmapfontname)
        index = (fullname, height)
        if index in fontnames:
            fontnames[index].append(bitmapfontname)
        else:
            fontnames[index] = [bitmapfontname]

    generate_fonts()
