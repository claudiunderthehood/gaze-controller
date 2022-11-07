import cv2
import mediapipe as mp
import pyautogui

class ECM:
    def __init__(self) -> None:
        pass
    
    def map(a,b,c,d,x):
        return(d*(x-a)+c*(b-x))/(b-a)
    
    def rightEye(landmarks,frame,frame_w,frame_h,screen_w,screen_h):
        right = [landmarks[473],landmarks[474],landmarks[475],landmarks[476],landmarks[477]]
        center = [landmarks[386],landmarks[362]]
        cx = center[0].x
        cy = center[1].y
        px = landmarks[473].x
        py = landmarks[473].y
        z = "Right Eye Off :("
        for id, landmark in enumerate(right):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            if id == 0:
                screen_x = ECM.map(cx-0.006,cx,0,screen_w,px)
                screen_y = ECM.map(cy-0.01,cy-0.007,0,screen_h,py)
                mousex, mousey = pyautogui.position()
                pyautogui.moveTo(ECM.map(0,1,mousex,screen_x,0.02), ECM.map(0,1,mousey,screen_y,0.005))
                z = "Rigth Eye On :)"
            else:
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
        return z
    
    def leftEye(landmarks,frame,frame_w,frame_h):
        z = "Left Eye Off :("
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.010:
            #pyautogui.click()
            pyautogui.doubleClick()
            pyautogui.sleep(1)
            z = "Left Eye On :)"
        return z

    def Camera(frame):
        cv2.imshow('ECM', frame)
        k = cv2.waitKey(1) & 0xFF #esc to quit
        if k == 27:
            cv2.destroyAllWindows()
            return True
        return False
        
    def main():
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
                ECM.rightEye(landmarks,frame,frame_w,frame_h,screen_w,screen_h)
                ECM.leftEye(landmarks,frame,frame_w,frame_h)   
            if(ECM.Camera(frame)):
                break

x=ECM
x.main()
