import math
import cv2
import sys
import time
from detect import detect_markers
from coding import decode, extract_hamming_code

#code to get the x, y, and z distance from a Hemming Marker perpendicular to the Hololen's Camera
def get_dist(perimeter):
        side_l = perimeter / 4
        cam_dist = 1561 * 12.3 / side_l
        return cam_dist

def get_scale_factor(perimeter):
        side_l = perimeter / 4
        coeff = 12.3 / side_l
        return coeff

def get_flat_offset(center, img_center, perimeter):
        x_off = center[0] - img_center[0]
        y_off = img_center[1] - center[1]
        scale = get_scale_factor(perimeter)
        sc_x = x_off * scale
        sc_y = y_off * scale

        #sc_x right of center
        #sc_y above center

        return sc_x, sc_y
def get_coordinates(marker, meters=True):
        #hololens center
        img_center = (640, 360)
        perim = marker.get_perimeter()
        center = marker.center()

        x, y = get_flat_offset(center, img_center, perim)
        dist = get_dist(perim)
        hyp = math.sqrt(x**2 + dist**2)
        if meters:
                x=round((x/100),1)  #modified for precise location
                y=round((y/100),1)
                dist= round(dist/100,1)
                print("dist: " + str(dist))

        return (x,y,dist)
def get_markers():
        #captures two frames then returns the ids of markers in both frames
        cap = cv2.VideoCapture("https://winlab:winlab89@10.50.250.152/api/holographic/stream/live_high.mp4?holo=false&pv=true&mic=false&loopback=false")
        ret, frame = cap.read()
        markers, ids = detect_markers(frame)
        ids_op = []
        for i in ids:
                ids_op.append(i)
        ord = []
		for a in markers:
                ord.append(get_coordinates(a, meters=True))
        return ids_op, ord
def get_from_frame():

        start = time.time()
        ctime = 0
        op = None
        op_ord = None
        count = 0
        ids, coordinates = get_markers()
        if len(ids) > 0:
                op = ids[0]
                op_ord = coordinates[0]
        else:
                op = 5000
                op_ord = (5000, 5000, 5000)
        ctime = time.time() - start
        print("returning..." + str(op))
        return op, op_ord
