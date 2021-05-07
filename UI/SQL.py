import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='wamit112233',
    database='testdatabase'
    )

mycursor = db.cursor()

#mycursor.execute('CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM("M", "F", "O") NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)')
#mycursor.execute("CREATE TABLE Users (username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)")
mycursor.execute("DELETE TABLE Users")

