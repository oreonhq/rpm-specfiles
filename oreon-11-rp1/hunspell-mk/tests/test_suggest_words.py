#!/usr/bin/python3

import enchant

wdlst = [ "здраво", "чај", "утрото"]
dic = enchant.Dict("mk_MK")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
