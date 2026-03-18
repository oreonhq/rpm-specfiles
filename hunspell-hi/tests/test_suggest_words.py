#!/usr/bin/python3

import enchant

wdlst = [ "नमस", "तरका", "चायत"]
dic = enchant.Dict("hi_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
