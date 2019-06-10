import os
import math
import re
from argparse import ArgumentParser
from collections import OrderedDict

from PIL import Image
import numpy as np
import scipy.misc

from Deep_Learning_StyleChange.stylize import  stylize

def imread(path):
    img = scipy.misc.imread(path).astype(np.float)
    # print(img)
    print(img.shape)
    if len(img.shape) == 2:
        # grayscale
        img = np.dstack((img,img,img))
    elif img.shape[2] == 4:
        # PNG with alpha channel
        img = img[:,:,:3]
    return img

# name="temp_test/"
# content="12-content.png"
# path="temp_test/12-content.png"
# content_image = imread("../"+path)

print(int("1000",20))
print(int("10101",2))
temp=[1,2,3,4,5]
print(temp[1:])