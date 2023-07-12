#! /usr/bin/python3

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import sys
import cv2

imgnp = np.asarray(Image.open(sys.argv[1]))
# img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
# imgnp = np.vstack(img)
imgplot = plt.imshow(imgnp)
new_image = nib.Nifti1Image(imgnp, affine=np.eye(4))
nib.save(new_image, sys.argv[2])