from PIL import Image
import os
import glob



    
os.chdir('/Users/herscdan/Documents/PRIVATE/GitHub/Westermosque')

image_names=glob.glob("scrapedcropped/*.jpg")



def resize_and_crop(img_path, size=(256,256)):

    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], size[0] * int(img.size[1] / img.size[0])),
                Image.ANTIALIAS)
        box = (0, (img.size[1] - size[1]) / 2, img.size[0], (img.size[1] + size[1]) / 2)
        
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((size[1] * int(img.size[0] / img.size[1]), size[1]),
                Image.ANTIALIAS)
        box = ((img.size[0] - size[0]) / 2, 0, (img.size[0] + size[0]) / 2, img.size[1])
        
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]), Image.ANTIALIAS)
        
    img.save(img_path)

#scale down images too 20x20 pixels
for i in image_names:
    resize_and_crop(i)