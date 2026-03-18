#!/usr/bin/python3

import enchant

wdlst = [ "сәлем", "шай", "таң"]
dic = enchant.Dict("kk_KZ")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
