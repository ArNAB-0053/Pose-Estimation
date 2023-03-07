import cv2
import mediapipe as mp
import time
import Pose_Estimation as PS

cap = cv2.VideoCapture('vdos/v004.mp4') # just give 0 in the braket then it will show as a live camera
pre_time = 0

detector = PS.PoseEstimation()
while True:
    succes, frame = cap.read()
    frame = detector.findPose(frame)
    lmList = detector.position(frame)
    print(lmList)

    # To follow any body parts__Here is Elbow
    # lmList = detector.position(frame, draw=False)
    # if len(lmList) != 0:
    #     print(lmList[14])
    #     cv2.circle(frame, (lmList[14][1], lmList[14][2]), 15, (159, 19, 75), cv2.FILLED)

    current_time = time.time()
    fps = 1/ (current_time-pre_time)
    pre_time = current_time
    
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    # Black Box
    start_point = (0, 0)
    end_point = (102, 32)
    color = (255, 255, 255)
    thickness = -1

    black_box = cv2.rectangle(frame, start_point, end_point, color, thickness) 

    cv2.putText(
        black_box,
        str(int(fps)),
        (31, 26),
        font, 1,
        (255, 200, 0),
        2
    )

    cv2.imshow("Camera", frame)
    if cv2.waitKey(10) == ord('0'):
        break
    
cap.release()
cv2.destroyAllWindows() 