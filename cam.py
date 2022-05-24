# # # created using OpenCV library to draw virtually on your webcam. Use a blue marker to draw your paintings. 
# # # *This works best with your webcam facing a white background!

import cv2
import numpy as np
from collections import deque

# Define upper and lower boundries for a colour to be blue.
blue_upper = np.array([140,255,255])
blue_lower = np.array([100,60,60])

#Define a 5x5 kernel for erosion and dialation
kernel = np.ones((5,5),np.uint8)

#Setup deques to store seperate colours in separate arrays
bpoints = [deque(maxlen = 512)]
gpoints = [deque(maxlen = 512)]
rpoints = [deque(maxlen = 512)]
ypoints = [deque(maxlen = 512)]

bindex = 0
gindex = 0
rindex = 0
yindex = 0

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
colour_index = 0

#setting up paint interface
paint_window = np.zeros((471,636,3)) + 255
paint_window = cv2.rectangle(paint_window,(40,1),(140,65),(0,0,0),2)
paint_window = cv2.rectangle(paint_window,(160,1),(255,65),colors[0],-1)
paint_window = cv2.rectangle(paint_window,(275,1),(370,65),colors[1],-1)
paint_window = cv2.rectangle(paint_window,(390,1),(485,65),colors[2],-1)
paint_window = cv2.rectangle(paint_window,(505,1),(600,65),colors[3],-1)
cv2.putText(paint_window,'CLEAR ALL',(49,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paint_window,'BLUE',(185,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,'GREEN',(298,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,'RED',(420,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,'YELLOW',(520,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(150,150,150),2,cv2.LINE_AA)

cv2.namedWindow('paint',cv2.WINDOW_AUTOSIZE)

#Load the Video
camera = cv2.VideoCapture(0)

while True:
    (grabbed,frame) = camera.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#Add the colouring option to the frame
    frame = cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame = cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame = cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame = cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame = cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)
    cv2.putText(frame,'CLEAR ALL',(49,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,'BLUE',(185,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'GREEN',(298,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'RED',(420,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'YELLOW',(520,33),cv2.FONT_HERSHEY_SIMPLEX,0.5,(150,150,150),2,cv2.LINE_AA)

    if not grabbed:
        break

    # Determine which pixels fall within the blue boundaries and then blur the binary image
    blueMask = cv2.inRange(hsv, blue_lower, blue_upper)   
    blueMask = cv2.erode(blueMask, kernel, iterations=2)
    blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, kernel)
    blueMask = cv2.dilate(blueMask, kernel, iterations=1)

    # Find contours in the image
    (cnts, _) = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # Check to see if any contours were found
    if len(cnts) > 0:

    # Sort the contours and find the largest one -- we
    # will assume this contour correspondes to the area of the bottle cap
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)

        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

        # Get the moments to calculate the center of the contour (in this case Circle)
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if center[1] <= 65:
            if 40 <= center[0] <= 140: #Clear All
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                bindex = 0
                gindex = 0
                rindex = 0
                yindex = 0
                paint_window[67:,:,:] = 255
            
            elif 160 <= center[0] <= 255:
                colour_index = 0 #BLUE
            
            elif 275 <= center[0] <= 370:
                colour_index = 1 #GREEN

            elif 390 <= center[0] <= 485:
                colour_index = 2 #RED

            elif 505 <= center[0] <= 600:
                colour_index = 3 #YELLOW

        else:
            if colour_index == 0:
                bpoints[bindex].appendleft(center)

            elif colour_index == 1:
                gpoints[gindex].appendleft(center)

            elif colour_index == 2:
                rpoints[rindex].appendleft(center)

            elif colour_index == 3:
                ypoints[yindex].appendleft(center)

    # Append the next deque when no contours are detected (i.e., bottle cap reversed)
    else:
        bpoints.append(deque(maxlen=512))
        bindex += 1
        gpoints.append(deque(maxlen=512))
        gindex += 1
        rpoints.append(deque(maxlen=512))
        rindex += 1
        ypoints.append(deque(maxlen=512))
        yindex += 1

    # Draw lines of all the colors (Blue, Green, Red and Yellow)
    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paint_window, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    # Show the frame and the paintWindow image
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paint_window)

    #If the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()