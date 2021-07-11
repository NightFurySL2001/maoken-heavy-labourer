#Warning: FontForge Python environment

import os
import fontforge
fontforge.loadNamelist('glyphlist.txt') # load a name list
import csv

#import xml.etree.ElementTree as ET #to read svg as xml and get width

#reopen last edited font
font = fontforge.open("shserif-maoken-heavy-labourer.sfd")

continue_num = 60303

input_path = "SourceHanSerifCN-Heavy-thicken.otf_svg_edit/"

#store width and lsb info
width = {}
lsb = {}
#read width file
with open("sourcehanserif_width.csv", "r", encoding="utf-8") as width_file:
    width_list = csv.reader(width_file)
    for row in width_list:
        width[row[0]] = int(row[1])
        lsb[row[0]] = int(row[2])

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
count=0
for filename in file_list:
    bname, ext =  os.path.splitext(filename)

    #skip already loaded files
    if bname==".notdef" or int(str(bname[3:])) <= continue_num:
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
    #glyph_tree = ET.parse(input_path+filename)
    #root = glyph_tree.getroot()
    #get width="xxxx px"
    #glyph_width=str(root.attrib['width'])
    #get digit before decimal point
    #glyph_width=glyph_width.split('.')[0]
    #glyph_tree = ""

    #move glyph to left if it had negative bearing, else do nothing
    if lsb[bname] < 0:
        glyph.transform((1,0,0,1,lsb[bname],0))
    #set glyph width
    glyph.width = width[bname]


    #simplify glyph
    glyph.simplify(8,("smoothcurves","ignoreslopes","nearlyhvlines","removesingletonpoints"))
    glyph.round()
    #deselect
    font.selection.none()
    count+=1
    if count%50 == 0:
        print(count)
    if count%2500 == 0:
        font.save('shserif-maoken-heavy-labourer.sfd')
        print("Last saved at: "+bname)
#font.selection.all()
#font.simplify()
#font.addExtrema()

print("Import complete.")
#generate font
font.save('shserif-maoken-heavy-labourer.sfd')
input("Finish. Press enter to exit.")
#font.generate("shserif-maoken-heavy-labourer.otf")
