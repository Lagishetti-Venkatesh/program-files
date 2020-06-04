from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0
def pic():
    camera.start_preview(alpha=200)
    sleep(9)# sleep time should be atleast 2 seconds to read the light levels
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
def video():
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
video()
#maximum camera features for capturing the image
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
camera.stop_preview()
