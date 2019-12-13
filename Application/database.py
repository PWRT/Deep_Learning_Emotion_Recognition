import pymysql

''' Database manager '''
# These class made for communicate with the MySQL database server
# Here were define the functions for execute the correct methodes
class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "emotiondb"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    # List in to the web page the content of the DB
    def list_emotions(self):
        self.cur.execute("SELECT *  FROM Emotions")
        result = self.cur.fetchall()
        return result

    # Insert into the DB a new value
    def insert_emotions(self, time, emotion):
        sql = "INSERT INTO Emotions (time, Emotion) VALUES (%s, %s)"
        val = (time, emotion)
        self.cur.execute(sql, val)
        self.con.commit()

    def emotions_count(self):
        result = self.cur.execute("SELECT * FROM Emotions WHERE id IS NULL")
        return result

    # Search in the database by date time
    # Web Logs page search
    def date_filter(self, start_time, stop_time):
        if start_time and stop_time:
            sql = "SELECT * FROM emotions WHERE DATE(Time) BETWEEN %s AND %s"
            val = (start_time, stop_time)
        else:
            sql = "SELECT * FROM emotions WHERE DATE(Time) = %s"
            val = start_time
        self.cur.execute(sql, val)
        result = self.cur.fetchall()
        return result

    # Number of the selected emotions
    def number_of_emotion(self, emotion):
        sql = "SELECT Count(Emotion) FROM emotions where Emotion = %s"
        val = emotion
        self.cur.execute(sql, val)
        result = self.cur.fetchall()
        return result