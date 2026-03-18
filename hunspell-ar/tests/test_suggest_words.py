#!/usr/bin/python3

import enchant

wdlst = [ "مرحبًا", "شاي", "صباح"]
dic = enchant.Dict("ar_EG")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
