import cv2
import numpy as np
import djitellopy as tello
import time

# instance of a class tello
my_drone = tello.Tello()

my_drone.connect()

print(my_drone.get_battery())

my_drone.streamon()
my_drone.takeoff()
my_drone.send_rc_control(0, 0, 25, 0)
time.sleep(2.2)

w, h = 480, 320

fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    MyfaceListC = []
    MyFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

        cx = x + w // 2
        cy = y + h // 2
        area = w * h

        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        MyfaceListC.append([cx, cy])
        MyFaceListArea.append(area)

    if len(MyFaceListArea) != 0:
        i = MyFaceListArea.index(max(MyFaceListArea))
        return img, [MyfaceListC[i], MyFaceListArea[i]]
    else :
        return img, [[0,0], 0]


def TrackFace(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    error = x - w // 2
    fb = 0
    speed = pid[0] * error + pid[1] * (error -pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0

    elif area > fbRange[1]:
        fb = -20

    elif area < fbRange[0] and area != 0 :
        fb = 20

    if x == 0:
        speed = 0
        error = 0

    my_drone.send_rc_control(0, fb, 0, speed)



while True:
    img = my_drone.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    info = findFace(img)

    pError = TrackFace(info, w, pid, pError)
    cv2.imshow("Output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        my_drone.land()
        break