import cv2

# Open the video file
cap = cv2.VideoCapture('2.mp4')

# Get the video's original height and width
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the desired height and width for the video
new_width = 200
new_height = 300

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('V2.mp4', fourcc, 20.0, (new_width, new_height))

# Loop through each frame of the video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Resize the frame to the desired height and width
        frame = cv2.resize(frame, (new_width, new_height))
        
        # Write the resized frame to the output video
        out.write(frame)
    else:
        break

# Release the video objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()
