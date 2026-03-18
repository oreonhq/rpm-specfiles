#!/usr/bin/python3

import enchant

wdlst = [ "ہیلو", "چائے", "چائے"]
dic = enchant.Dict("ur_PK")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
