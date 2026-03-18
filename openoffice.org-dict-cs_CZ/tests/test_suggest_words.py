#!/usr/bin/python3

import enchant

wdlst = [ "Hall", "čaj", "ráno"]
dic = enchant.Dict("cs_CZ")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
