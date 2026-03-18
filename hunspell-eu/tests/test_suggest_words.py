#!/usr/bin/python3

import enchant

wdlst = [ "Namak", "bidea", "Chait"]
dic = enchant.Dict("eu_ES")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))


