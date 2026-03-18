#!/usr/bin/python3

import enchant

wdlst = [ "привіт", "чай", "ранок"]
dic = enchant.Dict("uk_UA")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
