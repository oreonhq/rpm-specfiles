#!/usr/bin/python3

import enchant

wdlst = [ "hallo", "tee", "oggend"]
dic = enchant.Dict("ber_MA")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
