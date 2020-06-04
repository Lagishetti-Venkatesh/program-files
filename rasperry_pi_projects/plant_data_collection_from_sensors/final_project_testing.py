import RPi.GPIO as gp
import Adafruit_DHT
from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
import os
import imutils


lu = [
    [[13, 130, 186], [33, 150, 266]],
    [[13, 130, 184], [33, 150, 264]],
    [[13, 130, 184], [33, 150, 264]],
    [[12, 108, 181], [32, 128, 261]],
    [[8, 103, 182], [28, 123, 262]],
    [[11, 116, 158], [31, 136, 238]],
    [[7, 112, 150], [27, 132, 230]],
    [[5, 139, 116], [25, 159, 196]],
    [[2, 140, 101], [22, 160, 181]],
    [[1, 143,  88], [21, 163, 168]],
    [[-1, 182,  61], [19, 202, 141]],
    [[-4, 168,  63], [16, 188, 143]],
    [[-1, 160,  56], [19, 180, 136]],
    [[-2, 126,  46], [18, 146, 126]],
    [[-3, 163,  25], [17, 183, 105]],
    [[160,  54,   8], [180,  74,  88]],
    [[106, 109,   7], [126, 129,  87]],
    [[0, 198, 129], [20, 218, 209]],
    [[166, 245, 137], [186, 265, 217]],
    [[0, 198, 129], [20, 218, 209]],
    [[3, 245, 107], [23, 265, 187]],
    [[3, 245, 182], [23, 265, 262]],
    [[5, 189, 173], [25, 209, 253]],
    [[13, 245, 183], [33, 265, 263]],
    [[4, 161, 213], [24, 181, 293]],
    [[168,  65, 155], [188,  85, 235]]
]
#set the image address
img_address = '/home/venkatesh_lagishetti/plant_images/final_project_files/images'

#Raspbery pi camera settings
camera = PiCamera()
camera.rotation = 0
camera.resolution = (1000, 1000)
camera.start_preview(alpha=200)
sleep(2)# sleep time should be atleast 2 seconds to read the light levels
camera.capture(img_address+'/image.jpg')
camera.stop_preview()
#function to classifiy whether plant is healthy or not
def plant_health(location):
    images = list(os.listdir(location))
    try:
        for i in images:
            for luv in lu:
                dir = location +"/"+str(i)
                img = cv2.imread(dir)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                l = np.array(luv[0])
                u = np.array(luv[1])
                mask = cv2.inRange(hsv, l, u)
                tp = mask.shape[0] + mask.shape[1]  # total pixel values
                wv = np.count_nonzero(mask == 255)  # wv = white value

                #calculating the percetage of white pixels by total number of pixels and checking whether it is greater than 80% or not
                if((wv/tp*100) > 80):
                    os.remove(location +"/"+str(i))
                    prnit("After deleting the image",os.listdir(location +"/"+str(i)))
                    return 0
                else:
                    continue
            os.remove(location +"/"+str(i))
            print("After deleting the image", os.listdir(location +"/"+str(i)))
    except FileNotFoundError:
        pass
        return 1




# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

f = open('Data.csv', 'a')
#GPIO SETUP
moisture = 21
gp.setmode(gp.BCM)
gp.setup(moisture, gp.IN)
gpio=17
print('Moisture, Temperature(*C), Humidity', 'Plant Status')
for i in range(10):
    #collecting the data through the sensors.
    m = gp.input(moisture)
    status = plant_health(img_address)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    #converting data into string
    data = str(m) + ',' + str(humidity) + ',' + str(temperature) + ',' +str(status)+'\n'

    #Writing the Data into the file
    f = open('Data.csv', 'a')
    f.write(data)
    f.close()
    time.sleep(1)
