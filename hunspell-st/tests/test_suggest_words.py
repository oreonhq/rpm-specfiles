#!/usr/bin/python3

import enchant

wdlst = [ "Hall", "tee", "hoseng"]
dic = enchant.Dict("st_ZA")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
