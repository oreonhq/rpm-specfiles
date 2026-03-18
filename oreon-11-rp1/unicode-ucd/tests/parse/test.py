#!/usr/bin/env python3

codepoints = 0

file = '/usr/share/unicode/ucd/UnicodeData.txt'

with open(file, mode='rt', encoding='ascii') as unicode_data:
    for line in unicode_data.readlines():
        codepoint_string, name, category = line.split(';')[:3]
        codepoint = int(codepoint_string, 16)
        char = chr(codepoint)
        codepoints = codepoints + 1

print(codepoints)
# Unicode 17
assert(codepoints == 40575)
