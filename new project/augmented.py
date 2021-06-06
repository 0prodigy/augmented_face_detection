

# Load the cascade

# To capture video from webcam.

# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

# Read the frame

# youtube video or any other way to get all the frames

# step 0: get the video

# step 1: read this video using cv2
# step 2: resize the image

# we need to make a copy of original image, because if we don't then
# it will be stuck with the last frame for other person. If a user
# goes from person_1 -> person_2
# person_1 ka face will be stuck with the last frame for that video

# get face bounding box
# overlap the image
# UI
# Display
# Stop if escape key is pressed

# Release the VideoCapture object
