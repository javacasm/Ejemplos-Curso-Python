
'''
Proyecto: https://github.com/danielgatis/rembg
Tutorial: https://twitter.com/clcoding/status/1785357596922110421/photo/1

## instalación

pip install rembg
pip install pillow

'''

from rembg import remove
from PIL import Image

def remove_bg(input_path,output_path):

    in_image = Image.open(input_path)
    out_image = remove(in_image)
    out_image.save(output_path)
    Image.open(output_path)

remove_bg('./images/scully.jpeg','./images/scully_sin_bg.png')