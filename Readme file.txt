**_Project Title_**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Image to Text Converter Web Application


**_Description_**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This web application is used to extract any text present in an any type of image, and we can download extracted text into our local system in .txt or pdf file format.


**_Getting Started_**
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Installing**

1)This project has been developed using python version 3.9, so please install python 3.9 version.Download link is given below.
Download link: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

2)To run this application we need to install Tesseract into our local system. so please follow below download link and run command line in terminal
Download link:  [ https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
Command code to write in terminal: "pip install pytesseract"

3)For database MySql has been used, so we need to install into our local system. so please follow below download link and command link for treminal 
Download link: [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
Command code to write in terminal: "pip install mysql-connector"

4)Install requirements file. command to install requirement file is given below
command code to install: "pip install requirement"

5)please give your mysql host="localhost", user="********",password="*********",database="*******" names in "app.py" file.

**_Executing program_**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1)Please give Tesseract installation path in "Tesseract.py" file.
2)After running program check "record.log" where you will see "INFO werkzeug Thread-1 :  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)" 
3)Copy this url "http://127.0.0.1:5000/" from record.log and paste it on a browser.

**_Authors_**
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
M.Akhilesh

**_License_**
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project is licensed under the [M.Akhilesh]