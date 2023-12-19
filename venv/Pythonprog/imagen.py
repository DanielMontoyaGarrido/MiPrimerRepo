import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\danie\Imagenes\python.jpg",cv.IMREAD_COLOR)
img2 = cv.cvtColor(img,cv.COLOR_RGB2BGR)

# Matplotlib
plt.imshow(img)
plt.show()

# cv2
cv.imshow('Python',img2)
cv.waitKey(0)
cv.destroyAllWindows()


