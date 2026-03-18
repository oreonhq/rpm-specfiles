#! /usr/bin/python3

import gi
gi.require_version('LangTag', '0.6')
from gi.repository import LangTag

tag = LangTag.Tag.new()
if not tag.parse("en-Latn-US"):
    exit(1)

if tag.canonicalize() != 'en-US':
    exit(1)
