#!/usr/bin/python3

import enchant

wdlst = [ "saluton", "teo", "mateno"]
dic = enchant.Dict("eo_morf")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
