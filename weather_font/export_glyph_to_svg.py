from _typeshed import WriteableBuffer
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
output_path_png = font_name+"_png/"
try:
    os.mkdir(output_path_svg)
    os.mkdir(output_path_png)
except:
    print("Folder created")

# save file name for converting to png
filename_list=[]

glyph_set = font.getGlyphSet() #get all the glyphs
#loop through glyphs
for glyph_name in glyph_set.keys():
    #print(glyph_name)
    glyph = glyph_set[glyph_name]
    svg_path_pen = SVGPathPen(glyph_set)
    glyph.draw(svg_path_pen)

    #find metrics for svg
    ascender = font['OS/2'].sTypoAscender
    descender = font['OS/2'].sTypoDescender
    width = glyph.width
    ymin = font['head'].yMin
    ymax = font['head'].yMax
    height = ymax - ymin

    xstart = 0
    #check for zero width glyphs
    if width == 0:
        width = font['head'].xMax - font['head'].xMin
        xstart = font['head'].xMin
        print("Zero width glyph detected: "+glyph_name+". A full glyph based on xMin/xMax is exported.")

    #prepare svg contents
    content = dedent(f'''\
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="{xstart} {-ymax} {width} {height}">
                    <g transform="scale(1, -1)">
                        <path d="{svg_path_pen.getCommands()}"/>
                    </g>
                </svg>
            ''')
    
    #write content to svg file
    with open(output_path_svg + str(glyph_name) + ".svg", 'w') as f:
        f.write(content)
    filename_list.append(str(glyph_name) + ".svg")
