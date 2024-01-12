import cv2

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 30 frames / second
    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0,0)

    cv2.imshow('Gray', grayFrame)
    cv2.moveWindow('Gray', 600, 0)

    cv2.imshow('Camera2', grayFrame)
    cv2.moveWindow('Camera2', 0,400)

    cv2.imshow('Gray2', frame)
    cv2.moveWindow('Gray2', 600, 400)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()


