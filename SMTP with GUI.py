import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import os
from pathlib import Path
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from image_steganography import start

global location
location=[]
slide = tkinter.Tk()
slide.title("Login form")
slide.geometry('1080x1954')
slide.configure(bg='#222222')
slide = tkinter.Frame(bg='#222222')
    
def open_file():
    file = askopenfile(mode='r', filetypes=[('Image Files' ,'.jpeg'),('documents', '*pdf'),('Image Files' ,'*jpg'),('text' ,'.*txt'),('png' ,'.*png')])
    if file :
        filepath = os.path.abspath(file.name)
        tkinter.Label(slide, text="The File is located at : " + str(filepath), bg='#222222', fg="deeppink",font=('Aerial 11')).grid(column=1)
        location.append(filepath)
        print("Location of Selected file :",location)

def uploadFiles():
    tkinter.Label(slide, text='Files Uploaded Successfully!', bg='#222222',foreground='green',font=('Aerial 16')).grid(column=1,pady=10)

def SendMail():
    i=0
    path=location[0]
    path=r'{}'.format(path)
    with open(path, 'rb') as f:
        data = f.read()
    try:
        msg = MIMEMultipart()
        msg['Subject'] = subject_entry.get()
        msg['From'] =sender_entry.get()
        msg['To'] = receiver_entry.get()
        text = MIMEText(body_entry.get())
        msg.attach(text)

        mime_type, _ = mimetypes.guess_type(path)
        mime_type, mime_subtype = mime_type.split('/')
        print("Type of selected file :",mime_type)
        if mime_type=="image" or mime_type=="jpeg'":
            image = MIMEImage(data, name=Path(path).stem)
            msg.attach(image)
        elif mime_type=='text' or mime_type=='plain':
            text= MIMEText(data, name=Path(path).stem)
            msg.attach(text)
        elif mime_type=='audio' or mime_type=='basic':
            audio=MIMEAudio(data, name=Path(path).stem)
            msg.attach(audio)
        s = smtplib.SMTP(hostname_entry.get(),portno_entry.get())
        print("Connecting to servers.....")
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender_entry.get(),password_entry.get())
        print("trying to login....")
        s.sendmail(sender_entry.get(),receiver_entry.get(), msg.as_string())
        s.quit()
    except Exception as e:
        k=e
        i+=1
    if i>0:
        messagebox.showinfo(title="Failed", message="Unsuccessfull\nReason:{}".format(k))
        print("Unsuccessfull\nReason:{}".format(k))
        
    else:
        messagebox.showinfo(title="Successfully sent", message=" Mail sent successfully")
        print(" Mail sent successfully")

# Creating widgets
login_label = tkinter.Label(
    slide, text="MAIL THROUGH SMTP", bg='#222222', fg="cyan", font=("Arial", 30))
hostname_label = tkinter.Label(
    slide, text="Host Server", bg='#222222', fg="deeppink", font=("Arial", 16))
hostname_entry = tkinter.Entry(slide, font=("Arial", 16))
portno_label = tkinter.Label(
    slide, text="Port number", bg='#222222', fg="deeppink", font=("Arial", 16))
portno_entry = tkinter.Entry(slide, font=("Arial", 16))
sender_label = tkinter.Label(
    slide, text="Sender's Mail", bg='#222222', fg="deeppink", font=("Arial", 16))
sender_entry = tkinter.Entry(slide, font=("Arial", 16))
password_entry = tkinter.Entry(slide, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    slide, text="Password", bg='#222222', fg="deeppink", font=("Arial", 16))
receiver_label = tkinter.Label(
    slide, text="Receiver's Mail", bg='#222222', fg="deeppink", font=("Arial", 16))
receiver_entry = tkinter.Entry(slide, font=("Arial", 16))
subject_label = tkinter.Label(
    slide, text="Subject of Mail", bg='#222222', fg="deeppink", font=("Arial", 16))
subject_entry = tkinter.Entry(slide, font=("Arial", 16))
body_label = tkinter.Label(
    slide, text="Body of Mail", bg='#222222', fg="deeppink", font=("Arial", 16))
body_entry = tkinter.Entry(slide, font=("Arial", 16))
steg_label=tkinter.Label(
    slide, text="Steganography", bg='#222222', fg="deeppink", font=("Arial", 16))
enable = tkinter.Button(
    slide, text="Enable", bg="yellowgreen", fg="#222222",command=start)
file_label = tkinter.Label(
    slide, text="Attach files(<25MB)", bg='#222222', fg="deeppink", font=("Arial", 16))
filebtn = tkinter.Button(
    slide,text ="Choose File", bg="paleturquoise", fg="#222222", command = lambda:open_file())
upld = tkinter.Button(
    slide, text="Upload Files", bg="yellowgreen", fg="#222222",command=uploadFiles)
send_button = tkinter.Button(
    slide, text="Send mail", bg="cyan", fg="#222222", font=("Arial", 16), command=SendMail)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
hostname_label.grid(row=1,column=0)
hostname_entry.grid(row=1,column=1,pady=20)
portno_label.grid(row=2,column=0)
portno_entry.grid(row=2,column=1,pady=20)
sender_label.grid(row=3, column=0)
sender_entry.grid(row=3, column=1, pady=20)
password_label.grid(row=4, column=0)
password_entry.grid(row=4, column=1, pady=20)
receiver_label.grid(row=5,column=0)
receiver_entry.grid(row=5,column=1,pady=20)
subject_label.grid(row=6,column=0)
subject_entry.grid(row=6,column=1,pady=20)
body_label.grid(row=7,column=0)
body_entry.grid(row=7,column=1,pady=20)
steg_label.grid(row=8,column=0)
file_label.grid(row=9,column=0)
filebtn.grid(row=9,column=1)
upld.grid(row=9,column=2)
enable.grid(row=8,column=1)
send_button.grid(row=12, column=0, columnspan=2, pady=40)
slide.pack()
slide.mainloop()