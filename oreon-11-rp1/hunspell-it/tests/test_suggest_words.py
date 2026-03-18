#!/usr/bin/python3

import enchant

wdlst = [ "ciao", "tè", "mattina"]
dic = enchant.Dict("it_IT")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
