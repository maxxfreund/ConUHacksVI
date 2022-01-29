import cv2
import time
import os
import HandTrackingModule as htm
import WordGenerator as wg

tipIds = [4, 8, 12, 16, 20]


def countFin(lmList):
    fingers = []

    # Thumb
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingers.append(0)
    else:
        fingers.append(1)

    # 4 Fingers
    for i in range(1, 5):
        if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
            fingers.append(0)
        else:
            fingers.append(1)

    totalFingers = sum(fingers)

    # case A

    return totalFingers


def guessLetter(lmList):
    asciiCode = 0

    # Case A
    if lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] > lmList[5][1]:
        asciiCode = 65

    #Case B
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] < lmList[9][2] and lmList[16][2] < lmList[13][2] and lmList[20][2] < lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 66

    #Case C
    elif lmList[8][2] > lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] < lmList[3][1]:
        asciiCode = 67

    #Case D
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 68

    #Case E
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 69

    # Case F
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] < lmList[9][2] and lmList[16][2] < lmList[13][2] and lmList[20][2] < lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 70

    # Case G
    # Case H
    # Case I
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] < lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 73

    # Case J
    # Case K
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] < lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 75

    # Case L
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] > lmList[5][1]:
        asciiCode = 76

    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E
    # Case E




    #Case Z
    else:
        asciiCode = 64
    return asciiCode


def main():
    wCam, hCam = 1200, 1480

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "alpabet"
    myList = os.listdir(folderPath)
    # print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)

    # print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75)

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)  # list of all positions
        print(lmList)

        if len(lmList) != 0:
            # totalFingers = countFin(lmList)

            asciiLetter = guessLetter(lmList)

            h, w, c = overlayList[asciiLetter - 65].shape  # images
            img[0:h, 0:w] = overlayList[asciiLetter - 65]

            # cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
            # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
