#!/usr/bin/python3

import enchant

wdlst = [ "wita", "herbat", "poran"]
dic = enchant.Dict("pl_PL")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
