#import font subsetting
import sys
from fontTools import subset
from fontTools.ttLib import TTFont
import os

import rename_font
import get_font_item_list

#options for subsetter
def _get_default_options():
    opt = subset.Options()
    opt.name_IDs = ["*"]
    opt.name_legacy = True
    opt.name_languages = ["*"]
    opt.name_languages = ["*"]
    opt.layout_features = ["*"]
    opt.notdef_outline = True
    opt.recalc_bounds = False
    opt.recalc_timestamp = False
    opt.recommended_glyphs = True
    opt.drop_tables = []
    opt.glyph_names = True
    opt.legacy_cmap = True
    opt.symbol_cmap = True
    opt.prune_unicode_ranges = False
    return opt

#remove glyph that are not in remove_list
#output: glyph name list to be subset (final_font_list)
def subset_remove(font_char_list, font_glyph_list, simp_retain_list):
    #font_char_list format: (unicode dec, cid/glyph name, unicode name)
    #font_glyph_list format: (gid, glyph name)/(gid, cid)
    #simp_retain_list format: unicode dec
    
    final_font_list = [] #store final set of glyph name to be retained
    seen_list = [] #store already checked glyph names
    
    #loop through mapped chars first
    for item in font_char_list:
        id = item[0] #id
        glyph_name = item[1] #english glyph name/CID
        uni_name = item[2] #unicode glyph name

        #ignore non-cjk ideographs, leave them in final font
        if not (uni_name.startswith("CJK UNIFIED IDEOGRAPH") or uni_name.startswith("CJK COMPATIBILITY IDEOGRAPH")):
            final_font_list.append(glyph_name)
            seen_list.append(glyph_name)
            continue

        #check if id in retain list, if yes then add to subset list
        if id in simp_retain_list:
            final_font_list.append(glyph_name)
        
        #mark as seen
        seen_list.append(glyph_name)
    
    #then loop through unmapped glyphs and add them to subset list
    for (gid, glyph_name) in font_glyph_list:
        if glyph_name not in seen_list:
            final_font_list.append(glyph_name)
            seen_list.append(glyph_name)
    
    return final_font_list

#### END FUNC DEF
#### MAIN CODE START

font_file = "test.ttf"

simp_retain_list=[]
#open file with one character in one line, only cjk characters
#store: unicode dec
with open("simp-char-only.txt", "r", encoding="utf-8") as simp_list_file:
    for line in simp_list_file:
        simp_retain_list.append(ord(line.strip("\r\n")[0]))

#open font as TTFont resource
input_ttf = TTFont(font_file, 0,  allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

#get char list from font
#output: (unicode dec, cid/glyph name, unicode name)
font_char_list = get_font_item_list.get_unicode_cmap_list(input_ttf)
#get glyph list list from font
#output: (gid, glyph name)
font_glyph_list = get_font_item_list.get_glyph_name_list(input_ttf)

#close font
input_ttf.close()

#leave simp_retain_list, remove all other cjk ideographs
#do not touch non-cjk ideographs
#output: gid list
new_font_list = subset_remove(font_char_list, font_glyph_list, simp_retain_list)

#prepare for subsetting
print("Subsetting font...... please do not close while in progress.")

#font name use (id - original name - uuid .ttf/.otf)
new_font_name = font_file[:-4] + "-subset" + font_file[-4:]

#pyftsubset.exe .\sample-font-a.ttf --glyphs=A,B --output-file=sample-font-a-id.ttf 
#--layout-features=* --glyph-names --symbol-cmap --legacy-cmap
#--notdef-glyph --notdef-outline --recommended-glyphs --drop-tables=
#--name-IDs=* --name-legacy --name-languages=* --no-prune-unicode-ranges
options = _get_default_options()
#open font
font = subset.load_font(font_file, options)
#prepare subsetter
subsetter = subset.Subsetter(options)
#select all glyphs
subsetter.populate(glyphs=new_font_list)
#subset font
subsetter.subset(font)
#save font
subset.save_font(font, new_font_name, options)

print("Subset done. Font name: " + new_font_name)

#rename_font.add_font_suffix(new_font_name)

print("Completed.")