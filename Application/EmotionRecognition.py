import numpy as np
import cv2
from keras.models import load_model
from database import Database
import time

''' Emotion Recognition modul '''
# 1. Get the frame form camera
# 2. Find tha faces
# 3. With tha traind model predict the emotions
class EmotionRecognition(object):
    def __init__(self):
        self.emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}
        self.cap = cv2.VideoCapture(0)
        self.processed_frame = None
        self.detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # self.model._make_predict_function()
        print("[INFO] Starting...")

    # func for stream the video with the bounding boxes
    def get_processed_frame(self):
        return self.processed_frame

    # Process
    def run(self):
        # Load the model
        model = load_model('model.h5')
        db = Database()
        while True:
            # open camera and get frame to the further processing
            ret, frame = self.cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # detect faces in the grayscale frame
            faces = self.detector.detectMultiScale(gray, 1.3, 5)

            # From the found faces make further processing
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                roi_gray = gray[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
                # Predict from the croped faces frame
                prediction = model.predict(cropped_img)
                # if we have predictions insert the predicted emotion into the DB
                if (len(self.emotion_dict[int(np.argmax(prediction))]) > 1):
                    act_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    db.insert_emotions(act_time, self.emotion_dict[int(np.argmax(prediction))])
                # Put the predicted text over the rectangular around the detected face
                cv2.putText(frame, self.emotion_dict[int(np.argmax(prediction))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 255, 0), 1, cv2.LINE_AA)

            # Frame with preprocessed frame - rectangular + emotions text
            self.processed_frame = frame
