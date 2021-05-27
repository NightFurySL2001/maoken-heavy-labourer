from itertools import chain

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

input_file="SourceHanSansCN-Heavy.otf"

ttf = TTFont(input_file, 0, allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
#print(list(chars))

ttf.close()

char_count = 0
outfile = open(input_file+"-han.txt", 'w', encoding='utf-8')
lines_seen = []
for line in chars:
    if line[1] in lines_seen:
        continue
    #print(line)
    outfile.write(line[1]+"\n")
    char_count += 1
    lines_seen.append(line[1])
    

print("Done. Total glyphs: "+str(char_count))

# strip() only remove \n, \r is left in string
