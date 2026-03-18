#!/usr/bin/python3

import enchant

wdlst = [ "salve", "tea", "mane"]
dic = enchant.Dict("la")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
