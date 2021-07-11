import os

input_path = "SourceHanSerifCN-Heavy-thicken.otf_png_bmp_edit/"
output_path = "SourceHanSerifCN-Heavy-thicken.otf_svg_edit/"
try:
    os.mkdir(output_path)
except:
    print("Folder created")

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
count=0
for filename in file_list:
    bname, ext =  os.path.splitext(filename)
    os.system("potrace --turdsize 15 --unit 2 --opttolerance 0.28 --svg -o " + output_path + bname + '.svg -- ' + input_path + bname + '.bmp')
    count+=1
    if count%50 == 0:
        print("Traced " + str(count) +" pictures.")

print(str(count))