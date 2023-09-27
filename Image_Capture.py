from djitellopy import tello
from time import sleep
import cv2

# create an instance of the Tello class / create an object called my_drone
my_drone = tello.Tello()

# connect to the tello drone
my_drone.connect()

# prints the battery level of the drone
print(my_drone.get_battery())

# starts the video stream from the drone
my_drone.streamon()

while True :
    # Capture a frame from the video stream
    img = my_drone.get_frame_read().frame

    # display the captured frame using OpenCV
    cv2.imshow("Image", img)

    cv2.waitKey(1)

# it waits for a short time (1 ms) and listens to key press event.




