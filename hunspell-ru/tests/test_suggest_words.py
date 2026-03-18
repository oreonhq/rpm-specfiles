#!/usr/bin/python3

import enchant

wdlst = [ "прив", "чай", "утро"]
dic = enchant.Dict("ru_RU")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
