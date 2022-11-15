#pip install opencv-python
import cv2

cascade_face = cv2.CascadeClassifier('face_detector.xml') #add the xml file for face detection

cap = cv2.VideoCapture(0) #for capturing the video
while True:
  ret, img = cap.read() #read my video and read my image
  print(ret) #if it can read my face then True otherwise false
  g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert color from BGR to gray
  f = cascade_face.detectMultiScale(g,1.3,5) #detecting face
  for (x,y,w,h) in f: #for make a rectangle in face
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4) #creating custom rectangle

  cv2.imshow('img',img)
  k = cv2.waitKey(30) & 0xff
  if k==27:
    break
cap.release()
cv2.destroyAllWindows()

