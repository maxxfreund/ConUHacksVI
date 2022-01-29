import cv2
import time
import os
import HandTrackingModule as htm

tipIds = [4, 8, 12, 16, 20]


def countFingers(lmList):
    fingers = []

    # Thumb
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # 4 Fingers
    for i in range(1, 5):
        if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    totalFingers = sum(fingers)
    return totalFingers

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

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75)

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)  #list of all positions
        print(lmList)

        if len(lmList) != 0:
            totalFingers = countFingers(lmList)
            # print(totalFingers)

            h, w, c = overlayList[totalFingers - 1].shape
            img[0:h, 0:w] = overlayList[totalFingers - 1]

            cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()