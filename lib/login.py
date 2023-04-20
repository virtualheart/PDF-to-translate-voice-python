from tkinter import messagebox
import  sqlite3

class loginact():

    def log(user_name, password):
        if user_name == "" or password == "":
            messagebox.showerror(
                "Error", "Enter User Name And Password")
        else:
            try:
                conn = sqlite3.connect("db/data.db")
                cur = conn.cursor()
                query = "select * from ADMIN where username='" + \
                    user_name+"' and password='"+password+"'"
                # print(query)
                cur.execute(query)
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid User Name And Password")
                    return None

                else:
                    messagebox.showinfo(
                        "Success", "Successfully Login")
                    return True
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Dui to : {str(es)}")
                return False
            finally:
                conn.close()
