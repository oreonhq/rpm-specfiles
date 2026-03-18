#!/usr/bin/python3

import enchant

wdlst = [ "Óla", "xá", "dadeer"]
dic = enchant.Dict("tet_TL")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
