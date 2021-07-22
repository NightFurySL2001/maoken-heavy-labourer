import os

for count, filename in enumerate(os.listdir("SourceHanSerifCN-Heavy-thicken-hori.otf_bmp_edit")):
    if filename == ".notdef.bmp":
        continue

    id = filename[3:-4]
    dst = "cid" + str(id.rjust(5,"0")) + ".bmp"
    src ='SourceHanSerifCN-Heavy-thicken-hori.otf_bmp_edit/'+ filename
    dst ='SourceHanSerifCN-Heavy-thicken-hori.otf_bmp_edit/'+ dst
        
    # rename() function will
    # rename all the files
    os.rename(src, dst)
    #print(src+" "+ dst)