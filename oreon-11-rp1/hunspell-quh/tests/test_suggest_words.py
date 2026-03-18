#!/usr/bin/python3

import enchant

wdlst = [ "allinllac", "te", "tutap"]
dic = enchant.Dict("quh_BO")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
