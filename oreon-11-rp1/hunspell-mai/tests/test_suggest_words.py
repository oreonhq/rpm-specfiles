#!/usr/bin/python3

import enchant

wdlst = [ "अखा", "अंक", "मैथ"]
dic = enchant.Dict("mai_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
