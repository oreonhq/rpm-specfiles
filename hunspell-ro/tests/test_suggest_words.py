#!/usr/bin/python3

import enchant

wdlst = [ "Buna ziu", "ceai", "diminea"]
dic = enchant.Dict("ro_RO")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
