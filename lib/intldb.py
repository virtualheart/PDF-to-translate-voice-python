import sqlite3

conn = sqlite3.connect("db/data.db")

try:
    cursor = conn.execute("SELECT * from ADMIN limit 1")
except Exception as e:

    conn.execute("""
        CREATE TABLE ADMIN(
        ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
        USERNAME TEXT NOT NULL, 
        PASSWORD TEXT NOT NULL)
    """)
    print("Table ADMIN created successfully")

    conn.execute(
        "INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'admin789')")

    # conn.execute(
        # "INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('krazy', 'krazy789')")
    print("Username : admin\nPassword : admin789")
    conn.commit()

finally:
    conn.close()
