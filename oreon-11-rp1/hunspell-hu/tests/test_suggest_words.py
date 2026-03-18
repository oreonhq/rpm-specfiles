#!/usr/bin/python3

import enchant

wdlst = [ "Helló", "tea", "reggel"]
dic = enchant.Dict("hu_HU")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
