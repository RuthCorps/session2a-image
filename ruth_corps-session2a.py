from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import os

old_folder  = "/Users/rcorps/Documents/IMPRS Python/session_2 /session2a-image/raw"

new_folder = "/Users/rcorps/Documents/IMPRS Python/session_2 /session2a-image/processed"
#os.mkdir(new_folder)

img_list = os.listdir(old_folder)
print(img_list)

for item in img_list: # for each image in the list we've just specified 
    img_path = os.path.join(old_folder, item) # get the path
    filename, extension = os.path.splitext(img_path)
    img = Image.open(img_path) # open the image
    width = img.size[0]
    height = img.size[1]
    aspect_landscape = width / float(height)
    aspect_portrait = height / float(width)
    ideal_width_landscape = 400
    ideal_height_landscape = 300
    ideal_width_portrait = 300
    ideal_height_portrait = 400 
    ideal_aspect_l = ideal_width_landscape / float(ideal_height_landscape)
    ideal_aspect_p = ideal_width_portrait / float(ideal_height_portrait)
    if width > height and aspect_landscape > ideal_aspect_l:
        new_width = int(ideal_aspect_l *  height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
        orientation = 1
        new_img = img.crop(resize).resize((ideal_width_landscape, ideal_height_landscape), Image.ANTIALIAS)
    elif height > width and aspect_portrait > ideal_aspect_p:
        new_width = int(ideal_aspect_p * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
        orientation = 0 
        new_img = img.crop(resize).resize((ideal_width_portrait, ideal_height_portrait), Image.ANTIALIAS)
    elif width > height and aspect_landscape < ideal_aspect_l:
        new_height = int(width / ideal_aspect_l)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset)
        orientation = 1
        new_img = img.crop(resize).resize((ideal_width_landscape, ideal_height_landscape), Image.ANTIALIAS)
    else: 
        new_height = int(width / ideal_aspect_p)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset) 
        orientation = 0
        new_img = img.crop(resize).resize((ideal_width_portrait, ideal_height_portrait), Image.ANTIALIAS)
    new_img.save(os.path.join(new_folder, item + ".png"))



    

