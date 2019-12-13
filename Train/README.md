# Database

We used the fer2013 database from Kaggle.

It contains 48x48 pixel grayscale images of faces in seven categories.
(0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)

If you want to run the Jupyter notebook, please download the database:
[fer2013 database from Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

# Train

Created Convolutional neural networks and train the model.
Test the performance of the trained model.

* train_emotion_recognition_tfboard.ipynb - We trained the model with tensorboard
* train_emotion_recognition.ipynb - We changed the parameters and the network and get a better train result
* Hyperparameters_Optimization.ipynb - Finally we made some Hyperparameters Optimization, used hyperas and hyperopt python moduls

# Logs
* prediction.csv - Result of the training, the model runned on the test dataset
* model.h5 - The best trained emotion recognition weights 
* Weights found here: https://drive.google.com/drive/folders/1haoI-QBrXVWJQ2KH0hZ-npU9X5DDFHPS?usp=sharing
