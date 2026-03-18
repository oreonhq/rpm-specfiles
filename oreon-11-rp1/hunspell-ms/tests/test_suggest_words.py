#!/usr/bin/python3

import enchant

wdlst = [ "Hello", "teh", "pagi"]
dic = enchant.Dict("ms_MY")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
