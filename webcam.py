import cv2
cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out =  cv2.VideoWriter('sampleoutput.avi', fourcc,20,(640,480))
while True:
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow("video window", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
cap.release()
cv2.destroyAllWindows()
