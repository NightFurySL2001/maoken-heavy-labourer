#Warning: FontForge Python environment

import fontforge

font = fontforge.open("shs-maoken-heavy-labourer.sfd")

#move up all glyphs
font.transform((1,0,0,1,0,1012))
font.save('shs-maoken-heavy-labourer.sfd')