import os

# command line argument
import argparse


# Initialize parser
parser = argparse.ArgumentParser(description="convert one folder of bmp to another folder of svg")

# Adding optional argument
parser.add_argument("-i", "--input", help = "input folder name", required=True)
parser.add_argument("-o", "--output", help = "output folder name")

# Read arguments from command line
args = parser.parse_args()

input_path = args.input
output_path = args.output
#input_path = "SourceHanSansCN-Heavy.otf_bmp_edit/"
#output_path = "SourceHanSansCN-Heavy.otf_svg_edit/"

#turn to folder path
if not input_path.endswith("/"):
    input_path = input_path+"/"
#if no output path is specify
if output_path is None:
    output_path = input_path.split("_")[0]+"_svg_edit/"

try:
    os.mkdir(output_path)
except:
    print("Folder created")

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
count=0
for filename in file_list:
    bname, ext =  os.path.splitext(filename)

    #skip alrdy converted files
    if os.path.isfile(output_path + str(bname) + ".svg"):
        count+=1
        continue

    os.system('potrace --turdsize 15 --unit 2 --opttolerance 0.3 --svg -o "' + output_path + bname + '.svg" -i "' + input_path + bname + '.bmp"')
    count+=1
    if count%50 == 0:
        print("Traced " + str(count) +" pictures.")
