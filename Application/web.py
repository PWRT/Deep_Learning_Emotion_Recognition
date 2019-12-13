from threading import Thread
import cv2
from flask_basicauth import BasicAuth
from flask import Flask, url_for, flash, render_template, Response, request, redirect
from database import Database
import EmotionRecognition

''' Authenticaton setup '''
app = Flask(__name__)
app.secret_key = 'objectdetection'
app.config['BASIC_AUTH_USERNAME'] = 'DLBH'
app.config['BASIC_AUTH_PASSWORD'] = 'emotionrecognition'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

# Func for stream the webcam frame into the web page
def gen():
    global ERobj
    while True:
        stream = EmotionRecognition.EmotionRecognition.get_processed_frame(ERobj)
        ret, jpeg = cv2.imencode('.jpg', stream)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Start the main web page
@app.route('/')
def start():
    return render_template('welcome.html')

# Main page
@app.route('/index.html')
def video():
    return render_template('index.html')

# Video page
@app.route('/video_feed1')
def video_feed1():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Logs page with search
@app.route('/database.html', methods=['GET', 'POST'])
def Emotions():
    db = Database()
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        if not start_date and not end_date:
            ret = db.list_emotions()
            return render_template('database.html', result=ret, content_type='application/json')
        if not start_date and end_date:
            flash('Please fill the start time also!')
            ret = db.list_emotions()
            return render_template('database.html', result=ret, content_type='application/json')
        if start_date:
            ret = db.date_filter(start_date, end_date)
            return render_template('database.html', result=ret, content_type='application/json')
    else:
        ret = db.list_emotions()
        return render_template('database.html', result=ret, content_type='application/json')

# Evaluate page with statistic
@app.route('/evaluation.html')
def Logs():
    db = Database()
    ret_happy = db.number_of_emotion("Happy")
    ret_sad = db.number_of_emotion("Sad")
    ret_nat = db.number_of_emotion("Natural")
    ret_fear = db.number_of_emotion("Fear")
    ret_disg = db.number_of_emotion("Disgust")
    ret_angry = db.number_of_emotion("Angry")
    ret_surp = db.number_of_emotion("Surprise")
    ret = ret_happy + ret_sad + ret_nat + ret_fear + ret_disg + ret_angry + ret_surp
    return render_template('evaluation.html', result=ret, content_type='application/json')


# Run the second thread with the emotion recognition  thread
def RunSystem():
    # ------------Start the system ----------------
    global ERobj
    ERobj = EmotionRecognition.EmotionRecognition()
    t = Thread(target=ERobj.run, args=())
    t.daemon = True
    t.start()


# Run the web page - write into localhost:5000 to see the result in the browser
def run():
    RunSystem()
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
