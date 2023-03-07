import cv2
import time

# Open the video file
vdo = 'v004.mp4'
cap = cv2.VideoCapture(vdo)

# Get the video's original frame rate
original_fps = cap.get(cv2.CAP_PROP_FPS)

# Set the desired frame rate for the slow motion video
slow_motion_fps = original_fps / 2

# Get the video's original height and width
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f'Vdo[{vdo}]_slowmo.mp4', fourcc, slow_motion_fps, (original_width, original_height))

# Loop through each frame of the video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Write the current frame to the output video
        out.write(frame)
        
        # Display the frame for a specified duration to slow down the video
        time.sleep(1 / slow_motion_fps)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
