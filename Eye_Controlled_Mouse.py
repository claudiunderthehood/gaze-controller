import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    #print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        z = -1
        for landmark in landmarks:
            z+=1
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            cv2.putText(frame,str(z),(x,y),80,0.3,(255,0,0),1)
            #uso putText per vedere l'indice del landmark della pupilla
    cv2.imshow('ECM', frame)
    cv2.waitKey(1)