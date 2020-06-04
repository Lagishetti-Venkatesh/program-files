import numpy as np
import cv2
import os
import imutils
import time

address = '/home/venkatesh_lagishetti/plant_images/images'
list_of_img = os.listdir('/home/venkatesh_lagishetti/plant_images/images')


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


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized




def plant_health(location):
    health = {}
    images = list(os.listdir(location))
    for i in images:
        k = 0
        for luv in lu:
            dir = location +"/"+str(i)
            img = cv2.imread(dir)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            l = np.array(luv[0])
            u = np.array(luv[1])
            mask = cv2.inRange(hsv, l, u)
            tp = mask.shape[0] + mask.shape[1]  # total pixel values
            wv = np.count_nonzero(mask == 255)  # wv = white value

            if(wv/tp*100 > 80):
                health[i] = 0
                break
    return health
print('PLANT WILL BE LABELLED WHETHER IT IS HEALTHY OR NOT HEALTHY')
res = plant_health(address)
time.sleep(10)
plants = list(res.keys())

for i in list_of_img:
    if i in plants:
        cv2.imshow("NOT HEALTHY",image_resize(cv2.imread(address+"/"+(i)), 900, 900))
        print("NOT HEALTHY")
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        cv2.imshow("HEALTHY", image_resize(cv2.imread(address+"/"+(i)), 900, 900))
        print("HEALTHY")
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
