#!/usr/bin/python3

import enchant

wdlst = [ "Салам", "чай", "эртең менен"]
dic = enchant.Dict("ky_KG")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
