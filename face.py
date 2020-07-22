import cv2

cap = cv2.VideoCapture(0)  # 0 signifies that the feed is coming from our webcam
classifier = cv2.CascadeClassifier("C:\\Users\\hrtripathi\\Desktop\\haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()     #ret is just a binary/boolean variable that will be used for truthness
    if ret:
        faces = classifier.detectMultiScale(frame)
    # any image is accessed or modified using this synatx --> (__,__,__) and the range for these blanks/values of intensity go from 0 to 255
        for face in faces:
            x,y,w,h = face
            frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),3)

            cv2.imshow("output",frame)
    key = cv2.waitKey(30)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    

