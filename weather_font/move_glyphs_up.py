#Warning: FontForge Python environment

import fontforge

font_file_name = "shserif-maoken-heavy-labourer.sfd"

font = fontforge.open(font_file_name)

#move up all glyphs
font.selection.all()
font.transform((1,0,0,1,0,952))
font.save(font_file_name)