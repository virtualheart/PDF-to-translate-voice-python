import gtts
import os
# import playsound
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from translate import Translator
from PyPDF2 import PdfFileReader
# from tkPDFViewer import tkPDFViewer as pdf
# local libary
from lib.getsize import *
from lib.checkconnect import *
from lib.login import *
from lib.intldb import *

#------------------------------------------------------------------------------------------------------#

def deshboard():
	root=tk.Tk()
	root.title("TEXT TO SPEECH")
	root.geometry("1280x600")
	root.resizable(False,False)
	root.configure(bg="#305065")
	
	LANGUAGES = {'Tamil': 'ta', 'English': 'en','Hindi':'hi'}
	
	label_selected = tk.Label(root, text="null")
	a=tk.StringVar()
	Label(root,text="TEXT TO SPEECH",font="Helvetica 20 bold",fg="white",bg='#305065').pack(pady=10)
	auto_select=ttk.Combobox(root, values=list(LANGUAGES.keys()),width=27,textvariable=a,state='readonly',font=('verdana',10,'bold'))
	auto_select.set("Pick an language")
	auto_select.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=LANGUAGES[a.get()]))
	
	
	def browseFiles():
	    global filename
	    filename = filedialog.askopenfilename(initialdir = "/home/smk/Desktop/",title = "Select a File",filetypes = (("PDF Doc"," *.pdf"),("all files","*.*")))
	    label_file_explorer.configure(text=" "+filename)
	
	    PDFL1.configure(text=filename.split("/")[len(filename.split("/"))-1])
	    PDFL2.configure(text=getsize.file_size(filename))
	    
	    pdf = PdfFileReader(filename)
	    # information = pdf.getDocumentInfo()
	    number_of_pages = pdf.getNumPages()
	
	    PDFL3.configure(text=number_of_pages)
	    # PDFL4.configure(text=filename)
	
	
	def pdftotext(pdf_path):
	    
	    with open(pdf_path, 'rb') as f:
	        pdf = PdfFileReader(f)
	        # information = pdf.getDocumentInfo()
	        number_of_pages = pdf.getNumPages()
	
	        text=''
	        for i in range(0,number_of_pages):
	                # creating a page object
	                pageObj = pdf.getPage(i)
	                # extracting text from page
	                text=text+pageObj.extractText()
	    return text
	
	def translate():
	    pb.start()
	    if not checkconnect.connect():
	        pb.stop()
	        return False 
	
	    try:
	        lang_1=pdftotext(filename)
	        
	        v=lang_1.split(".")
	
	        cl=label_selected.cget("text")
	    except Exception as e:
	        messagebox.showerror("TEXT TO SPEECH","Please select PDF file")
	        pb.stop()
	        return False
	
	
	    if lang_1 == '' or cl == 'null':
	        messagebox.showerror("TEXT TO SPEECH","Please select language")
	        pb.stop()
	
	    else:
	        dest_txt.delete(1.0,END)
	        translator=Translator(to_lang=cl)
	        output=translator.translate(lang_1) 
	        dest_txt.config(state= NORMAL)
	        dest_txt.delete(1.0,'end')
	        dest_txt.insert('end',output)
	        dest_txt.config(state= DISABLED)
	
	        tts = gtts.gTTS(text=output, lang=cl)
	        tts.save("eAudio.mp3")
	        # playsound.playsound("eAudio.mp3")
	        pb.stop()
	
	        os.system("cvlc eAudio.mp3 vlc://quit")
		        
	    # Create a File Explorer label
	label_file_explorer = Label(root, text = "Select PDF File",width = 65, height = 1,)
	    
	PDFL1=Label(root, text = "",width = 65, height = 1,bg='#305065')
	PDFL2=Label(root, text = "",width = 65, height = 1,bg='#305065')
	PDFL3=Label(root, text = "",width = 65, height = 1,bg='#305065')
	# PDFL4=Label(root, text = "",width = 65, height = 1,bg='#305065')
	
	PDFL1.place(x=145,y=175)
	PDFL2.place(x=145,y=215)
	PDFL3.place(x=145,y=255)
	# PDFL4.place(x=145,y=305)
	
	pb = ttk.Progressbar(root,orient='horizontal',mode='indeterminate',length=280)
	pb.place(x=850,y=500)
	    
	dest_txt=Text(root,width=40,height=15,borderwidth=2,relief=RIDGE,font=('verdana',15),state= DISABLED)
	dest_txt.place(x=710,y=110)
	    
	
	#Textboxes & Buttons
	auto_select.place(x=150,y=60)
	# TamilText="வணக்கம்.அறம் செய விரும்பு, ஆறுவது சினம், இயல்வது கரவேல், ஈவது விலக்கேல், உடையது விளம்பேல். நன்றி!"
	
	button_change=Button(root,text="TRANSLATE",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',cursor=" hand2", command=translate)
	button_change.place(x=590,y=540,width=100,height=40)
	# button_clear=Button(root,text="CLEAR",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',cursor="hand2",command=clear)
	# button_clear.place(x=590,y=480,width=100,height=40)
	
	button_explore = Button(root,text = "Browse Files",command = browseFiles)
	
	button_explore.place(x=30,y=110)
	label_file_explorer.place(x=150,y=114)
	Label(root,text="Filename  : ",font="Helvetica 12 bold",fg="white",bg='#305065').place(x=30,y=175)
	Label(root,text="PDF Size  : ",font="Helvetica 12 bold",fg="white",bg='#305065').place(x=30,y=215)
	Label(root,text="PageCount : ",font="Helvetica 12 bold",fg="white",bg='#305065').place(x=30,y=255)
	# Label(root,text="PDF       : ",font="Helvetica 12 bold",fg="white",bg='#305065').place(x=30,y=305)
    
#------------------------------------------------------------------------------------------------------#
# login moduals
	
def main():
	def clear():
		userentry.delete(0,END)
		passentry.delete(0,END)

	def close():
	    win.destroy() 

	def log():
		if loginact.log(user_name.get(),password.get()):
			close()
			deshboard()

	win = Tk()

	# app title
	win.title("TEXT TO SPEECH")

	# window size
	win.maxsize(width=500 ,  height=500)
	win.minsize(width=500 ,  height=500)
	
	#heading label
	heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
	heading.place(x=80 , y=150)
	
	username = Label(win, text= "User Name :" , font='Verdana 10 bold')
	username.place(x=80,y=220)
	
	userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
	userpass.place(x=80,y=260)
	
	# Entry Box
	global user_name
	global password
	
	user_name = StringVar() 
	password = StringVar()   

	userentry = Entry(win, width=30 , textvariable = user_name)
	userentry.focus()
	userentry.place(x=200 , y=223)
	    

	passentry = Entry(win, width=30, show="*" ,textvariable = password)
	passentry.place(x=200 , y=260)
	        
	# button login and clear
	    
	btn_login = Button(win, text = "Login" ,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',cursor=" hand2", command = log)
	btn_login.place(x=200, y=293)
	    
	btn_login = Button(win, text = "Clear" ,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',cursor=" hand2", command = clear)
	btn_login.place(x=266, y=293)
	    
	win.mainloop()

#------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
	main()
	
