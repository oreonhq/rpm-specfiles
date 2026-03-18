#!/usr/bin/python3

import enchant

wdlst = [ "dhit", "ca", "maid"]
dic = enchant.Dict("ga_IE")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
