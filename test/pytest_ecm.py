from Eye_Controlled_Mouse import ECM
import pyautogui
import mediapipe as mp
import cv2
import time

def test_map():
    assert ECM.map(0,10,0,100,2)==20

def test_rightEye():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape 
    if landmark_points:
        landmarks = landmark_points[0].landmark
        print(ECM.rightEye(landmarks,frame,frame_w,frame_h,screen_w,screen_h))
        assert ECM.rightEye(landmarks,frame,frame_w,frame_h,screen_w,screen_h)=="Rigth Eye On :)"
    
def test_leftEye():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape 
    if landmark_points:
        landmarks = landmark_points[0].landmark
        print(ECM.leftEye(landmarks,frame,frame_w,frame_h))
    if (landmarks[145].y - landmarks[159].y) < 0.010:
        assert ECM.leftEye(landmarks,frame,frame_w,frame_h)=="Left Eye On :)"
    else:
        assert ECM.leftEye(landmarks,frame,frame_w,frame_h)=="Left Eye Off :("

def test_Camera():
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame,1)
        k=ECM.Camera(frame)
        if(k):
            break
    assert k==True
    
test_map()
test_rightEye()
test_leftEye() #prova occhio aperto
time.sleep(1) #(o viceversa)
test_leftEye() #prova occhio chiuso
test_Camera()        