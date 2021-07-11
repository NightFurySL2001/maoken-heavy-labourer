#import font subsetting
import sys
from fontTools import subset
from fontTools.ttLib import TTFont
import os

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

font_file = "SourceHanSerifCN-Heavy.otf"
#use original file as subsetting cid

simp_retain_list=[]
#open file with one character in one line, only cjk characters
#store: unicode dec
with open("../build_final_otf_sans/simp-char-only.txt", "r", encoding="utf-8") as simp_list_file:
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

output = open("SC/map-subset-SC.txt", "w", encoding="utf-8")
output.write("mergeFonts\n")
output.write("0\t.notdef\n")
seen_list=[]
for gid in new_font_list:
    if gid.startswith(".") or gid == "nonmarkingreturn" or gid in seen_list:
        continue
    cid = int(str(gid[3:]))
    output.write(str(cid) + "\t" + str(gid) + "\n")
    seen_list.append(gid)