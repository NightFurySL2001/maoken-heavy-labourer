cid_code=open("raw-shs.txt","r",encoding="utf-16be")
edited_list=open("raw.txt","r",encoding="utf-16le")

cid_array = []
for line in cid_code:
    cid_array.append(line.strip("\r\n"))

edit_array = []
for line2 in edited_list:
    edit_array.append(line2.strip("\r\n"))

cid_code.close()
edited_list.close()

raw_combined_list = open("raw-final.txt","w",encoding="utf-8")
resource_map_list = open("map-final.txt","w",encoding="utf-8")
for line_no in range(len(cid_array)):
    cid_number = cid_array[line_no].split("\t")
    glyph_number = edit_array[line_no].split("\t")
    raw_combined_list.write(cid_number[0]+"\t"+glyph_number[0]+"\t"+cid_number[0]+"\t"+glyph_number[2]+"\n")
    resource_map_list.write(cid_number[0]+"\t"+glyph_number[2]+"\n")