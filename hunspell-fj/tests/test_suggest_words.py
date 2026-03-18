#!/usr/bin/python3

import enchant

wdlst = [ "Bula", "ti", "mataka"]
dic = enchant.Dict("fj_FJ")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
