import sqlite3

# edit this
uname="admin"
pw="admin789"

conn = sqlite3.connect("db/data.db")

try:

    cursor = conn.execute("SELECT * from ADMIN limit 1")

except Exception as e:

    try:
        conn.execute("""
            CREATE TABLE ADMIN(
            ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
            USERNAME TEXT NOT NULL, 
            PASSWORD TEXT NOT NULL)
        """)
        print("Table ADMIN created successfully")
        
        qur="INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('" + uname + "','" + pw +"')"

        conn.execute(qur)

        print("Username : "+ uname +"\nPassword : "+pw )
        conn.commit()
    
    except Exception as e:
        print(e)
    finally:
        conn.close()

finally:
    conn.close()
