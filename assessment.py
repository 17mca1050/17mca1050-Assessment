Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk
import tkinter as tk
import smtplib
from email.message import EmailMessage

mainwin = Tk()
mainwin.title("WELCOME TO CHANDIGARH UNIVERSITY")
mainwin.configure(bg='white')

v_address = tk.StringVar(mainwin)
v_subject = tk.StringVar(mainwin)

def email_content():
    message = txt_message.get("1.0", "end-1c")
    address = v_address.get()
    subject = v_subject.get()
    email = EmailMessage()
    email['from'] = ‘AKSHAY BHATIA'
    email['to'] = address
    email['subject'] = subject
    email.set_content = message
    send_mail(email)


def send_mail(emai):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(‘uic.17mca1050@gmail.com', 'akshay_543')
        smtp.send_message(emai)


# staring of heading
heading = ttk.Label(mainwin, text="E-Mail App", font='arial 18 bold')

heading.config(foreground='RED', background='white')

heading.place(x=320, y=30)

ttk.Separator(mainwin).place(y=101, relwidth=1)

# start of label and input types widgets

lbl_name = ttk.Label(mainwin, text="To: ",font='arial 14 bold').place(x=190, y=118)

txt_address = ttk.Entry(mainwin, textvariable=v_address, width=80).place(x=250, y=120)

lbl_subject = ttk.Label(mainwin, text="Subject: ", font='arial 14 bold').place(x=140, y=150)

txt_subject = ttk.Entry(mainwin, textvariable=v_subject,width=80).place(x=250, y=150)


lbl_message = ttk.Label(mainwin, text="Message: ", font='arial 14 bold').place(x=140, y=200)

txt_message = Text(mainwin, width=60, height=10)

txt_message.insert("end", "")

txt_message.place(x=250, y=200)

send_btn = ttk.Button(mainwin, text=' Send Now ', command=email_content ).place(x=250, y=400)

mainwin.geometry('800x800')
mainwin.mainloop()
