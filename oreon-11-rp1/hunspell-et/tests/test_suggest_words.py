#!/usr/bin/python3

import enchant

wdlst = [ "tere", "tee", "hommikul"]
dic = enchant.Dict("et_EE")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
