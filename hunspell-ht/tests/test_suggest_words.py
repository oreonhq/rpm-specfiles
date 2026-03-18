#!/usr/bin/python3

import enchant

wdlst = [ "bonjou","te", "maten"]
dic = enchant.Dict("ht_HT")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
