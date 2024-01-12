import cv2

width = 640
height = 360
myRadius = 30
myColor = (0,0,0) # black
thickness = 2

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

    #frame[140:220, 250:390] = (255,0,255)
    # When thickness is -1 then fill
    cv2.rectangle(frame, (250,140), (390,220), (0,255,0), -1)               # rectangle(frame, upper left, lower right, color, thickness)
    cv2.circle(frame, (width//2, height//2), myRadius, myColor, thickness)    # circle(frame, center, radius, color, thickness)

    cv2.imshow('title', frame)
    cv2.moveWindow('title', 0, 0)
                  
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
   

