#!/usr/bin/python3

import enchant

wdlst = [ "Hall", "ti", "moning"]
dic = enchant.Dict("tpi_PG")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
