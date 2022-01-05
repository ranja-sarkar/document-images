
#LIBRARIES
import fitz 
import time
import os


def extract_images(filename):
    ''' Function that defines the method of image extraction from .pdf (editable) file.'''
    
    doc = fitz.open(filename)
    dir_name = str(filename[:-4])
    out_path = os.path.join("C:/Users/Ranja.Sarkar/documents", dir_name)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    print('Output dir/folder of images created.')
    
    imgcount = 0
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                imgcount += 1
                if pix.n > 5:
                    name = out_path + 'p%s-%s.jpg' %(i, xref)
                    pix.save(name)
                else:
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    name = 'p%s-%s.jpg' %(i, xref)
                    output = os.path.join(out_path, name)
                    pix1.save(output)
                    pix1 = None 
                #pix = None
            except:
                print('Error encountered at file.')
        
    return print("Number of images extracted = ", imgcount)

extract_images("DL_flow.pdf")
print("Time taken (s) = ", round(time.perf_counter(), 2))


'''
##PIL can be used to view the images
from PIL import Image
from pylab import *

img = array(Image.open('p0-99.jpg'))
imshow(img)
'''



