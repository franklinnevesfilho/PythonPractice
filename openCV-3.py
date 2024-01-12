import cv2

width = 320
height = 180
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # telling cv2 we are displaying the image
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)    # Set the width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # Set the height
cam.set(cv2.CAP_PROP_FPS, 30)         # set fps
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # set codec and format 'moving jpg'

def displayWindow(title, frame, pos):
    cv2.imshow(title, frame)
    cv2.moveWindow(title, pos[0], pos[1])

while True:
    _, frame = cam.read()

    cv2.imshow('title', frame)
    cv2.moveWindow('title', 0, 0)
                  
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
   

