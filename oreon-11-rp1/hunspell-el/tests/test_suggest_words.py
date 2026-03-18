#!/usr/bin/python3

import enchant

wdlst = [ "Γειά σου", "τσάι", "πρωί"]
dic = enchant.Dict("el_GR")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
