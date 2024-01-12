import cv2
print(cv2.__version__)


cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 30 frames / second
    cv2.imshow('Camera', grayFrame)
    cv2.moveWindow('Camera', 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

