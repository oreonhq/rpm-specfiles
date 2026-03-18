#!/usr/bin/python3

import enchant

wdlst = [ "Hall", "tè", "filgħodu"]
dic = enchant.Dict("mt_MT")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
