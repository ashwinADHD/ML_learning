
from PIL import Image
import numpy as np

#reading image 

img = Image.open('500.png').convert('L')#monocrome
img.save('result21.png')

image_array = np.array(img)
#since image is 255.0 bit, in order to normalize them we have to divide image_array with 255 bit
image_array = image_array / 255.0

print (image_array.shape)

#establishing Kernal and strides
#establish output matrix using (n-f+1) x (n-f+1)
#i.e. n is dimentional, f is kernal size in same direction as dim

Kernel= np.array([[1,0,-1],[2,0,-2],[3,0,-3]])
stride=1
output = np.zeros((498,498))
output1 =np.zeros((498,498))
B0 = image_array[0:3,0:3]
k=0

for i in range(498):
    
    #B = image_array[0:3,0+i:3+i]
    
    for j in range(498):
            C = image_array[0+j:3+j,0+i:3+i]
            piece_wise = np.multiply(C,Kernel)
            output[i,j]=np.sum(piece_wise) 
         
#we are rescalling the image for the final output for convolutional layer
rescaled = (255.0 / output.max() * (output - output.min())).astype(np.uint8)
#image has be transposed so we are using transpose on rescaled image 
rescaled = rescaled.T
im=Image.fromarray(rescaled)
im.save('convolutional_output_2.png')



