# Database

We used the fer2013 database from Kaggle.

It contains 48x48 pixel grayscale images of faces in seven categories.
(0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)

If you want to run the Jupyter notebook, please download the database:
[fer2013 database from Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

# Train

Convolutional neural networks were trained and tested with Keras moduls.

* train_emotion_recognition_tfboard.ipynb - We trained the model with tensorboard
* train_emotion_recognition.ipynb - We changed the parameters and the network and get a better train result
* Hyperparameters_Optimization.ipynb - Finally we made some Hyperparameters Optimization, used hyperas and hyperopt python moduls

**Training steps:**
* Preparing database:
	* Load the csv with pandas modul
	* visualized the dataset
	* did some image augmentation to balanced the dataset
	* prepare the augmented dataset for training and testing
* Create a model with Keras:
	* Used Convolusion layers, Danse, dropout, Batchnormalization
* Did some hyperparameters optimalizations for a better performance 
* Tested the traind model with the prepared test dataset
* Exported the best model for the emotion recognition application


# Logs
* prediction.csv - Result of the training, the model runned on the test dataset
* model.h5 - The best trained emotion recognition weights 
* Weights found here: https://drive.google.com/drive/folders/1haoI-QBrXVWJQ2KH0hZ-npU9X5DDFHPS?usp=sharing
