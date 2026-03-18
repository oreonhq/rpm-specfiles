#!/usr/bin/python3

import enchant

wdlst = [ "ସ୍ବାତ", "ନସ୍କର ", "ଓଡ଼ଆ"]
dic = enchant.Dict("or_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
