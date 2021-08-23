
import pyshorteners
from tkinter import *
#import string
root=Tk()
root.title("Url shortener")
root.geometry("300x300")
root.configure(bg='lightblue')
Label(root,text="Enter Url :",font=("times","16"),padx=8,pady=4).grid(row=1,column=2)
url_input=Entry(root,font=("times","20"))
url_input.grid(row=2,column=2,pady=25,padx=10)
str_url=StringVar(root)
shortened_url=Label(root,textvariable=str_url,font=("times","20"))
shortened_url.grid(row=4,column=2,pady=25)
def short_url():
   try:
      s=pyshorteners.Shortener()
      url=url_input.get()
      res=s.tinyurl.short(url)
      str_url.set(res)
      url_input.delete(0,END)
   except:
      str_url.set("Please Ente url !!")
btn=Button(root,text="Short url",padx=8,pady=4,font=("times","16"),background="pink",command=short_url)
btn.grid(row=3,column=2,pady=6)

mainloop()