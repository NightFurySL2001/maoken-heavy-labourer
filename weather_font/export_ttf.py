#Warning: FontForge Python environment

import fontforge

font = fontforge.open("shserif-maoken-heavy-labourer.sfd")

print("Exporting font....")
font.generate("shserif-maoken-heavy-labourer.ttf")

font.close()
input("Finish. Press enter to exit.")