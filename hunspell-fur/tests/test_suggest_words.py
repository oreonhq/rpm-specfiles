#!/usr/bin/python3

import enchant

wdlst = [ "mandi" , "te" , "matine"]
dic = enchant.Dict("fur_IT")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
