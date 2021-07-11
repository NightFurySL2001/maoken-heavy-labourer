#Warning: FontForge Python environment

import fontforge

font = fontforge.open("SourceHanSerifCN-Heavy.otf")

font.selection.all()
font.changeWeight(10,"CJK")
print("Exporting font....")
font.save()
font.generate("shs-cn-thicken.otf")

font.close()
input("Finish. Press enter to exit.")