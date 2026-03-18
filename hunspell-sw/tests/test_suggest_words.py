#!/usr/bin/python3

import enchant

wdlst = [ "habari", "chai", "asubuhi"]
dic = enchant.Dict("sw_TZ")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
