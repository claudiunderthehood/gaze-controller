import cv2
import mediapipe as mp
import pyautogui

def map(a,b,c,d,x):
    return(d*(x-a)+c*(b-x))/(b-a)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size() 
while True: 
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        right = [landmarks[473],landmarks[474],landmarks[475],landmarks[476],landmarks[477]]
        center = [landmarks[386],landmarks[362]]
        cx = center[0].x
        cy = center[1].y
        px = landmarks[473].x
        py = landmarks[473].y
        for id, landmark in enumerate(right)  :
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            if id == 0:
                screen_x = map(cx-0.003,cx+0.003,0,screen_w,px)
                screen_y = map(cy-0.005,cy+0.005,0,screen_h,py)
                pyautogui.moveTo(screen_x,screen_y)
            else:
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.010:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('ECM', frame)
    cv2.waitKey(1)