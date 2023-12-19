import cv2 as cv
video = cv.VideoCapture(1)

while(video.isOpened()):
    ret,frame = video.read()
    if ret == True:
        cv.imshow('video casero', frame)
        key = cv.waitKey(1)

        if (key == ord('q')):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
    



