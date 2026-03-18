#!/usr/bin/python3

import enchant

wdlst = [ "नमस", "अभि", "यथात"]
dic = enchant.Dict("ne_NP")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
