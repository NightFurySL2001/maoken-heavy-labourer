from itertools import chain

from fontTools.unicode import Unicode

def get_unicode_cmap_list(ttfont_var):
    #input:TTFont variable
    #output:list of (unicode dec, glyph name, unicode name) (for glyf font)
    #output:list of (unicode dec, cid, unicode name) (for CID font)

    #format:(unicode dec, glyph name, unicode name)
    chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttfont_var["cmap"].tables)
    
    #remove duplicate lines
    return_list=[]
    seen_list=[]
    for item in chars:
        if item[0] not in seen_list:
            return_list.append(item)
            seen_list.append(item[0])

    #testing checks
    #file=open("test-cmap.txt","w",encoding="utf-8")
    #for row in return_list:
    #    print(row)
    #    file.write("%s\n" % str(row))

    return return_list

def get_glyph_name_list(ttfont_var):
    #input:TTFont variable
    #output:list of (glyph id, glyph name)

    #return glyph names
    glyphs = ttfont_var.getGlyphOrder()
    
    #store for use
    return_list=[]
    #convert to (glyph id, glyph name) by directly adding number
    for gid, glyph_name in enumerate(glyphs):
        return_list.append([gid,glyph_name])

    #testing checks
    #file=open("test-glyph.txt","w",encoding="utf-8")
    #for row in return_list:
    #    print(row)
    #    file.write("%s\n" % str(row))

    return return_list
