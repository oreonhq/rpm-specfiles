import fontforge
import os

myFont = fontforge.open("Cantarell-Regular.ttf")
myFont.generate("Cantarell-Regular.sfd")
myFont.close()

myFont = fontforge.open("Cantarell-Regular.sfd")
myFont.generate("Cantarell-Regular.ttf")
myFont.close()

os.remove("Cantarell-Regular.ttf")
os.remove("Cantarell-Regular.sfd")

