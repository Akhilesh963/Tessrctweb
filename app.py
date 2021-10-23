from importlib import reload
from flask import Flask
from flask import request,render_template
from Tesseract import pytesseract
from PIL import Image
import os,cv2
import sys
reload(sys)
from flask_mysqldb import MySQL
import mysql.connector
import logging



app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submitImage/',methods=['GET', 'POST'])
def submitImage():
    if request.method == 'POST':
        file = request.files['ocrImage']
        app.logger.info('selecting image')
        app.logger.info('selecting image'+ str(file))
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)

        image = cv2.imread(UPLOAD_FOLDER + "/" + file.filename)
        os.remove(UPLOAD_FOLDER + "/" + file.filename)
        app.logger.debug("converting!")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, 3)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        custom_config = r'-l eng+jpn --psm 6'
        app.logger.info('text extracting.....')
        app.logger.warning('Warning level log')
        text = pytesseract.image_to_string(Image.open(filename),lang="eng",config=custom_config)
        app.logger.info('Extracted text is :' + text)
        app.logger.info('text extracted!')
        os.remove(filename)
        print(text)
    try:
        app.logger.warning('checking connection.....')
        mydb = mysql.connector.connect(
            host="localhost",
            user="Akhilesh",
            password="Akhilesh63!$",
            database="uploads")
        app.logger.info('connected to Database!')
        cursor = mydb.cursor()
        create_table = """CREATE TABLE HI(id INT  NOT NULL AUTO_INCREMENT PRIMARY KEY , files Text NOT NULL) """
        cursor.execute(create_table)
        mydb.commit()
        mydb.close()
    except mysql.connector.Error as error:
        app.logger.error(format(error))
        print(format(error))
    return render_template('textFile.html',text=text)



if __name__ == '__main__':
    app.run(threaded=True, debug=True)
