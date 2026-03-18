#!/usr/bin/python3

import enchant

wdlst = [ "ola", "cha", "manh"]
dic = enchant.Dict("pt_PT")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
