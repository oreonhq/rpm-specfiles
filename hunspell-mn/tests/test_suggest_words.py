#!/usr/bin/python3

import enchant

wdlst = [ "сайн уу", "цай", "өглөө"]
dic = enchant.Dict("mn_MN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
