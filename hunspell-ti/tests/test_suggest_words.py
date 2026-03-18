#!/usr/bin/python3

import enchant

wdlst = [ "ሰላም", "ሻሂ", "ጉሓት"]
dic = enchant.Dict("ti_ER")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
