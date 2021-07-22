#from _typeshed import WriteableBuffer
from re import X
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import os #create folder
from textwrap import dedent #output svg

#import font name
font_name = "SourceHanSansCN-Heavy.otf"

#open font file with fonttools
font = TTFont(font_name)
#make folder to output
output_path_svg = font_name+"_svg/"
try:
    os.mkdir(output_path_svg)
except:
    print("Folder existed")

# save file name for converting to png
filename_list=[]

glyph_set = font.getGlyphSet() #get all the glyphs

#find full metrics using fontbbox (prevent edge cutting)
xmin = font['head'].xMin
xmax = font['head'].xMax
#width = xmax - xmin
ymin = font['head'].yMin
ymax = font['head'].yMax
height = ymax - ymin

width_record = open("sourcehansans_width.csv", "w", encoding="utf-8")

#loop through glyphs
for glyph_name in glyph_set.keys():

    #print(glyph_name)
    glyph = glyph_set[glyph_name]
    svg_path_pen = SVGPathPen(glyph_set)
    glyph.draw(svg_path_pen)

    #find metrics and store for later
    width = glyph.width
    glyph_width = width

    xstart = 0
    #see if glyph have point exceed left side
    if glyph.lsb < 0:
        xstart = glyph.lsb
        glyph_width = width+abs(xstart)
    #check for zero width glyphs
    if width == 0:
        glyph_width = xmax - xmin
        xstart = xmin
        print("Zero width glyph detected: "+glyph_name+". A full glyph based on xMin/xMax is exported.")
    
    width_record.write(glyph_name+","+str(width)+","+str(xstart)+"\n")

    #skip alrdy converted files
    if os.path.isfile(output_path_svg + str(glyph_name) + ".svg"):
        continue

    #prepare svg contents, add 100px to width so right edge wont get cut, wont affect result since stored in file
    content = dedent(f'''\
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="{xstart} {-ymax} {glyph_width+100} {height}">
                    <g transform="scale(1, -1)">
                        <path d="{svg_path_pen.getCommands()}"/>
                    </g>
                </svg>
            ''')

    #write content to svg file
    with open(output_path_svg + str(glyph_name) + ".svg", 'w') as f:
        f.write(content)
    filename_list.append(str(glyph_name) + ".svg")

width_record.close
