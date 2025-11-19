import os
from dotenv import load_dotenv
import pymysql

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = int(os.getenv('DB_PORT', '3306'))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'job_portal_db')

print(f"Connecting to MySQL at {DB_HOST}:{DB_PORT} as {DB_USER}")

try:
    conn = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, autocommit=True)
    cur = conn.cursor()
    print(f"Dropping database '{DB_NAME}' if it exists...")
    cur.execute(f"DROP DATABASE IF EXISTS `{DB_NAME}`;")
    print(f"Creating database '{DB_NAME}'...")
    cur.execute(f"CREATE DATABASE `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print("Done.")
    cur.close()
    conn.close()
except Exception as e:
    print("Error while resetting database:", e)
    raise
