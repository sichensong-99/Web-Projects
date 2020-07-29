import sqlite3 #导入SQLite驱动
# pylint: disable=no-member
conn = sqlite3.connect('ssc.db') #若该db不存在，则自动创建
print("Opened database successfully")

conn.execute('CREATE TABLE user1 (name TEXT, email TEXT, password TEXT,age TEXT,gender TEXT,feedback TEXT,experience TEXT,checkbox TEXT)')
print("Table created successfully")
conn.close() #关闭connection