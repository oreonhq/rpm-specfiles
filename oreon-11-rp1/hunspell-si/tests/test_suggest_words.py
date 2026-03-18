#!/usr/bin/python3

import enchant

wdlst = [ "පේ", "හලෝ", "සිංල"]
dic = enchant.Dict("si_LK")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
