# Python program to explain cv2.cvtColor() method  
   
# importing cv2  
import cv2  
   

# Reading an image in default mode 
src = cv2.imread(r"C:\Users\danie\Imagenes\geeks14.png",8) 
print(type(src))
print(src)
# Window name in which image is displayed 
window_name = 'Image'
  
# Using cv2.cvtColor() method 
# Using cv2.COLOR_BGR2HSV color space 
# conversion code 
image = cv2.cvtColor(src,cv2.IMREAD_GRAYSCALE) 

print(cv2.IMREAD_UNCHANGED)
print(cv2.IMREAD_GRAYSCALE)
  
# Displaying the image  
if(image is not None):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is none")


