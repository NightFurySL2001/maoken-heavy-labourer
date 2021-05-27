#Warning: FontForge Python environment

import os
import fontforge
fontforge.loadNamelist('glyphlist.txt') # load a name list

import xml.etree.ElementTree as ET #to read svg as xml and get width

#reopen last edited font
font = fontforge.open("shs-maoken-heavy-labourer.sfd")

input_path = "SourceHanSansCN-Heavy.otf_svg_edit_smaller/"

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
count=0
for filename in file_list:
    bname, ext =  os.path.splitext(filename)

    #skip already loaded files
    if bname==".notdef" or int(str(bname[3:])) <= 43751:
        count+=1
        continue

    try:
        if bname.startswith("uni"):
            #for glyph named uniXXXX, convert to base 10
            glyph = font.createChar(int(bname[3:],16),bname)
        else:
            #for named glyphs font
            glyph = font.createMappedChar(bname)
    except:
        #for cid key
        glyph = font.createChar(-1, bname)
    try:
        glyph.importOutlines(input_path+filename,scale=False)
    except:
        print("Error. Glyph name: " + bname)
    
    #parse the svg
    glyph_tree = ET.parse(input_path+filename)
    root = glyph_tree.getroot()
    #get width="xxxx px"
    glyph_width=str(root.attrib['width'])
    #get digit before decimal point
    glyph_width=glyph_width.split('.')[0]

    #set glyph width
    glyph.width = int(glyph_width)
    
    glyph_tree = ""

    #simplify glyph
    glyph.simplify(8,("smoothcurves","ignoreslopes","nearlyhvlines","removesingletonpoints"))
    glyph.round()
    #deselect
    font.selection.none()
    count+=1
    if count%50 == 0:
        print(count)
    if count%2500 == 0:
        font.save('shs-maoken-heavy-labourer.sfd')
#font.selection.all()
#font.simplify()
#font.addExtrema()

print("Import complete.")
#generate font
font.save('shs-maoken-heavy-labourer.sfd')
input("Finish. Press enter to exit.")
#font.generate("shs-maoken-low-wage.otf")
