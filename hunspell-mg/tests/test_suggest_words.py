#!/usr/bin/python3

import enchant

wdlst = [ "Salama", "dite", "MARAINA"]
dic = enchant.Dict("mg_MG")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
