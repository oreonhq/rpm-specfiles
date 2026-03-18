#!/usr/bin/python3

import enchant

wdlst = [ "բարև", "թեյ", "առավոտ"]
dic = enchant.Dict("hy_AM")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
