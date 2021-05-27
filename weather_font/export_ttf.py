#Warning: FontForge Python environment

import fontforge

font = fontforge.open("shs-maoken-heavy-labourer.sfd")

print("Exporting font....")
font.generate("shs-maoken-low-wage.otf")

font.close()
input("Finish. Press enter to exit.")