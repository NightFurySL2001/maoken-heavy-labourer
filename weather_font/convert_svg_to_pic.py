
from cairosvg import svg2png 
import os

input_path = "SourceHanSerifCN-Heavy-thicken.otf_svg/"
output_path = "SourceHanSerifCN-Heavy-thicken.otf_png/"
try:
    os.mkdir(output_path)
except:
    print("Folder existed")

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
for filename in file_list:
    #split filename to name and extension (eg "random.svg" to "random", ".svg")
    bname, ext =  os.path.splitext(filename)

    #skip alrdy converted files
    if os.path.isfile(output_path + bname + '.png'):
        continue

    try:
        svg2png(url=input_path + bname + '.svg', write_to=output_path + bname + '.png')
    except:
        print(filename)
    #os.system("cairosvg -f png -o " + output_path_png + bname + '.png ' + output_path_svg + bname + '.svg')