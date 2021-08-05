

from PIL import Image
import numpy as np

#read in image
img = Image.open('tree(2).png').convert('L') #inout image is 10x10 and converted into monocrome
img.save('result1.png')

image_array = np.array(img)

print (image_array)

#establishing Kernal and strides
#establish output matrix using (n-f+1) x (n-f+1)
#i.e. n is dimentional, f is kernal size in same direction as dim

Kernel= np.array([[1,0,-1],[2,0,-2],[3,0,-3]])
stride=1
output = np.zeros((8,8))
B0 = image_array[0:3,0:3]
k=0
for i in range(8):
# B = image_array[0:3,0+i:3+i]
for j in range(8):
C = image[0+j:3+j,0+i:3+i]
piece_wise_multi = np.multiply(C,Kernel)
# while k < len(z):
output[i,j]=np.sum(piece_wise_multi)

