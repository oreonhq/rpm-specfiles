#!/usr/bin/python3

import enchant

wdlst = [ "helo", "te", "boreu"]
dic = enchant.Dict("cy_GB")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
