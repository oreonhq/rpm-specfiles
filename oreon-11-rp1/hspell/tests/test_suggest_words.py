#!/usr/bin/python3

import enchant

wdlst = [ "שלום", "תֵה", "שַׁחַר"]
dic = enchant.Dict("he_IL")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
