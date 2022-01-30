import cv2
import time
import os
import HandTrackingModule as htm
from WordGenerator import *

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

    # Case R
    if lmList[8][1] < lmList[12][1] and lmList[4][1] < lmList[5][1]:
        asciiCode = 82
        # Case S
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[10][1] and lmList[4][2] < lmList[10][2]:
        asciiCode = 83
    # Case A
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][
        2] > lmList[17][2] and lmList[4][1] > lmList[5][1]:
        asciiCode = 65

    # Case B
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] < lmList[9][2] and lmList[16][2] < lmList[13][2] and lmList[20][2] < lmList[17][2] and lmList[4][1] < lmList[5][1] and lmList[8][2] < lmList[7][2]:
        asciiCode = 66

    # Case C
    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] > lmList[5][1] and lmList[4][2] < lmList[5][2]:
        asciiCode = 67

    # Case E
    elif lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] > lmList[16][2]:
        asciiCode = 69



    # Case N
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] < lmList[13][2]:
        if lmList[4][1] > lmList[9][1]:
            asciiCode = 84
        elif lmList[4][1] < lmList[13][1]:
            asciiCode = 77
        else:
            asciiCode = 78

    # to do
    # Case O
    elif lmList[8][2] > lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 79


    # Case P
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[0][2] and lmList[14][2] > lmList[13][2] and lmList[18][
        2] > lmList[17][2] and lmList[4][1] < lmList[2][1]:
        asciiCode = 80

    # Case Q
    elif lmList[8][2] > lmList[0][2] and lmList[10][2] > lmList[9][2] and lmList[14][2] > lmList[13][2] and lmList[18][
        2] > lmList[17][2] and lmList[4][2] > lmList[0][2]:
        asciiCode = 81


    elif lmList[8][1] > lmList[4][1] and lmList[10][1] > lmList[9][1]:
        if lmList[12][1] > lmList[4][1]:
            asciiCode = 72 # Case H
        else:
            asciiCode = 71 # Case G


    # Case J
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][
        2] < lmList[17][2] and lmList[4][1] > lmList[5][1]:
        asciiCode = 74

    # Case D
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][
        2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 68

    # Case F
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] < lmList[9][2] and lmList[16][2] < lmList[13][2] and lmList[20][
        2] < lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 70

    # Case I
    elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][
        2] < lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 73

    # Case K, V, U
    elif lmList[16][2] > lmList[13][2] and lmList[20][2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        if (lmList[8][2] < lmList[5][2]) and lmList[12][2] < lmList[9][2] and lmList[4][2] < lmList[5][2]:
            asciiCode = 75 #k
        elif lmList[5][1] < lmList[8][1] and lmList[12][1] < lmList[9][1]:
            asciiCode = 86 #v
        else:
            asciiCode = 85 #u

    # Case L
    elif lmList[8][2] < lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2] and lmList[20][
        2] > lmList[17][2] and lmList[4][1] > lmList[5][1]:
        asciiCode = 76

    # Case W
    elif lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][
        2] > lmList[17][2] and lmList[4][1] < lmList[5][1]:
        asciiCode = 87

    # Case X
    elif lmList[8][2] > lmList[7][2] and lmList[8][1] > lmList[7][1] and lmList[10][1] > lmList[9][1] and lmList[14][
        1] > lmList[13][1] and lmList[18][1] > lmList[17][1]:
        asciiCode = 88

    # Case Y
    elif lmList[20][1] < lmList[17][1] and lmList[4][1] > lmList[5][1] and lmList[4][2] < lmList[5][2] and lmList[12][2] > lmList[9][2] and lmList[16][2] > lmList[13][2]:
        asciiCode = 89

    # Case Z
    else:
        asciiCode = 90

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
    text = chooseWord()
    letter_list = []
    guess_list = []

    word = str(text).upper()
    print("Word",word)
    # print("len",len(word))
    display_list = []
    for i in range(len(word)):
        display_list.append("_")
    a = " ".join(display_list)

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (700, 80)
    fontScale = 2
    color = (0, 0, 255)
    thickness = 1
    tries = 0
    while True:
        if "_" not in display_list:
            print("Winner! Winner! Chicken Dinner!")
            main()
        if tries >= 6:
            main()

        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)  # list of all positions
        #print(lmList)

        if len(lmList) != 0:
            # totalFingers = countFin(lmList)

            asciiNum = guessLetter(lmList)
            asciiLetter = str(chr(asciiNum))
            letter_list.append(asciiLetter)
            if letter_list.count(asciiLetter) > 75:
                letter_list.clear()
                guess_list.append(asciiLetter)
                print(asciiLetter)
                print("count", word.count(asciiLetter))
                if word.count(asciiLetter) == 1:
                    print("hit")
                    index = word.find(asciiLetter)
                    display_list[index] = asciiLetter
                    a = " ".join(display_list)

                    cv2.putText(img, a, org, font, fontScale, color, thickness, cv2.LINE_AA)
                elif word.count(asciiLetter) > 1:
                    print("more hit")
                    for i in range(len(word)):
                        if word[i] == asciiLetter:
                            display_list[index] = asciiLetter
                            a = " ".join(display_list)
                            cv2.putText(img, a, org, font, fontScale, color, thickness, cv2.LINE_AA)
                else:
                    tries += 1
                    print("Wrong Letter!")


            h, w, c = overlayList[asciiNum - 65].shape  # images
            img[0:h, 0:w] = overlayList[asciiNum - 65]



        # Nelly


        cv2.putText(img, a, org, font, fontScale, color, thickness, cv2.LINE_AA)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
