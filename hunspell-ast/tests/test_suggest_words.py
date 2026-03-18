#!/usr/bin/python3

import enchant

wdlst = [ "Hola", "té", "mañana"]
dic = enchant.Dict("ast_ES")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
