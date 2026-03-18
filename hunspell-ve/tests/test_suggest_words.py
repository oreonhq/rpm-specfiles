#!/usr/bin/python3

import enchant

wdlst = [ "Ndumeliso", "tie", "matsheloni"]
dic = enchant.Dict("ve_ZA")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
