import cv2 as cv
video = cv.VideoCapture(r"C:\Users\danie\Imagenes\video1.mp4")

while(True):
    ret,frame = video.read()
    if ret:
        cv.imshow('video casero', frame)
        if cv.waitKey(30) == ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()




