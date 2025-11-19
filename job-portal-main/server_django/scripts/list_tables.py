import os
from dotenv import load_dotenv
import pymysql

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
DB_HOST=os.getenv('DB_HOST')
DB_PORT=int(os.getenv('DB_PORT'))
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
print('Connecting:',DB_HOST,DB_PORT,DB_USER,DB_NAME)
conn=pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,database=DB_NAME)
cur=conn.cursor()
cur.execute('SHOW TABLES')
print('Tables in',DB_NAME,':')
for r in cur.fetchall():
    print(' -',r[0])
cur.close(); conn.close()
