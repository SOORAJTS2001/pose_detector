from itertools import count
import cv2 as cv
from cv2 import FONT_HERSHEY_COMPLEX
import cvzone as cvz
from cv2 import VideoCapture
import mediapipe as mp
import PositionModule as pm
import random
count = 0
cap = cv.VideoCapture(0)#records video from the camera
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = cv.flip(img,1)#it is to flip the image
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[11])
        print(lmList[12])
        #img pos is the position coordinates of the image as a dictionary with key as name of the image,
        # print(lmList[16])
        cv.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 255, 0), cv.FILLED)
    # angle = detector.findAngle(img, 16, 14, 12, draw=False)
    # print(angle)
    # fpsReader = cvz.FPS()
    # print(hb,wb)
    # cv.namedWindow("Image", cv.WND_PROP_FULLSCREEN)
    # cv.setWindowProperty("Image", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    # _, imgResult = fpsReader.update(imgResult)
    cv.imshow("Image", img)
    cv.waitKey(1)