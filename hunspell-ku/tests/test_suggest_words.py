#!/usr/bin/python3

import enchant

wdlst = [ "Slav", "çay", "sib"]
dic = enchant.Dict("ku_TR")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
