#!/usr/bin/python3

import enchant

wdlst = [ "សួស្តី", "តែ", "ព្រឹក"]
dic = enchant.Dict("km_KH")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
