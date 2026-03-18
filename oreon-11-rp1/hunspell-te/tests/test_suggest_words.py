#!/usr/bin/python3

import enchant

wdlst = [ "లో", "మది", "తెగు"]
dic = enchant.Dict("te_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
