#!/usr/bin/python3

import enchant

wdlst = [ "დილა მშვიდობისა", "გამარჯობა" ,"ჩაი"]
dic = enchant.Dict("ka_GE")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
