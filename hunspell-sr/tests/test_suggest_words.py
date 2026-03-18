#!/usr/bin/python3

import enchant

wdlst = [ "здрав", "чај", "јутро"]
dic = enchant.Dict("sr_YU")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
