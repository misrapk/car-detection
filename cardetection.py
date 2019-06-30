import cv2
car_cascade = cv2.CascadeClassifier('E:\piyush\coding\Training Ducat\documents of ml\cars.xml')
path = input("enter path of video: ")

cam = cv2.VideoCapture(path)
text = "car"
count = 0

while True:
    ret, frame= cam.read()
#     print(ret)
    count +=1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car = car_cascade.detectMultiScale(gray, 1.1,5)
    
    for (x,y,w,h) in car:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0,250),2)
#         count+=1
#         print(x)
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),1)
    cv2.imshow("videoDetection", frame)
    if cv2.waitKey(30) == 27:
        break
        
cv2.destroyAllWindows()