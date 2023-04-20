from tkinter import messagebox
try:
    import httplib  # python < 3.0
except:
    import http.client as httplib


class checkconnect():

    def connect():
        conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
        try:
            conn.request("HEAD", "/")
            return True
        except Exception:
            messagebox.showerror(
                "TEXT TO SPEECH", "Pleace Check the internet connection")
            return False
        finally:
            conn.close()
