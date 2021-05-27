import os

#editing picture
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint, seed


input_path = "SourceHanSansCN-Heavy.otf_png/"
output_path = input_path[:-1]+"_bmp_edit/"
try:
    os.mkdir(output_path)
except:
    print("Folder created")

files = os.listdir(input_path)
file_list = [f for f in files if os.path.isfile(os.path.join(input_path, f))]
for filename in file_list:
    #split filename to name and extension (eg "random.svg" to "random", ".svg")
    bname, ext =  os.path.splitext(filename)
    #open image, convert to RGBA
    png = Image.open(input_path+filename).convert('RGBA')
    png.load() # required for png.split()

    #create white background and paste pic to turn alpha to white background
    img = Image.new("RGB", png.size, (255, 255, 255))
    img.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    
    #close image
    png.close()

    #get image width/height
    width, height = img.size
    #prepare drawing
    draw = ImageDraw.Draw(img)

    # Let's have repeatable, deterministic randomness
    #seed(37)

    # Draw a random number of circles around 400-800, if upm >= 2000 use 1000-1500
    cmin = randint(900, 1200)
    cmax = randint(1300, 1800)
    
    for _ in range(cmin,cmax):
        #radius size in px
        diam = randint(25,45)

        #position
        x, y = randint(0,width), randint(0,height)

        #add ellipse into picture, fill white
        draw.ellipse([x,y,x+diam,y+diam], fill=(255,255,255))

    #prepare threshold
    thresh = 200
    fn = lambda x : 255 if x > thresh else 0

    # Blur the background a bit
    blur = img.filter(ImageFilter.BoxBlur(12))

    #resharpen image (2x) after blur, convert to black & white
    sharpened1 = blur.filter(ImageFilter.SHARPEN);
    sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);
    res = sharpened2.convert('L').point(fn, mode='1')

    # Save result
    res.save(output_path+bname+'.bmp')

    #close image
    img.close()