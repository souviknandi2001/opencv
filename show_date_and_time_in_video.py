import  cv2
import datetime

video = cv2.VideoCapture(0);

while True:
    date=str(datetime.datetime.today())
    print(date)
    #print(date)
    front = cv2.FONT_ITALIC
    ret, frame = video.read()
    frame= cv2.putText(frame,date,(20,50),front,1,(23,23,230),2,cv2.LINE_8)
    cv2.imshow("video window" ,frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
