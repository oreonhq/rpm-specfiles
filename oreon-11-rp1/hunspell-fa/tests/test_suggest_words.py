#!/usr/bin/python3

import enchant

wdlst = [ "Hey", "te", "morgun"]
dic = enchant.Dict("fa_IR")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
