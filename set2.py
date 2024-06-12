from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

window = Tk()
window.title("Information")
window.geometry("{0}x{0}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
Label(window,text="Job Application",font=('Helvetica 24 bold'),fg="black").place(relx=0.5, rely=0.03,anchor=CENTER)
Label(window,text="Personal Information", font="Helvetica 16 bold",fg="red").grid(row=1,column=1,pady=(40,0))
Label(window,text="Name: ", font="Helvetica 14").grid(row=2,column=1)

text1 = Entry(window,width=40)
text1.insert(0,'First Name')
text1.grid(row=2,column=2)
 
text2 = Entry(window,width=40)
text2.insert(0,'Last Name')
text2.grid(row=2,column=3,padx=(20,0))
Label(window,text="Email: ", font="Helvetica 14").grid(row=3,column=1)
 
text3 = Entry(window,width=40)
text3.insert(0,'user@example.com')
text3.grid(row=3,column=2,)

Label(window,text="Education: ", font="Helvetica 14").grid(row=4,column=1)
dropdown1 = tk.StringVar(value="Please Choose") 
education_chosen = ttk.Combobox(window,width=37,textvariable=dropdown1,state="readonly") 
  
# Adding combobox drop down list 
education_chosen['values'] = (' Primary School',  
                          ' Secondary School', 
                          ' Higher-Secondary School', 
                          " Undergraduate/Bachelor's", 
                          " Postgraduate/Master's", 
                          ' Doctoral/Ph.D') 
  
education_chosen.grid(row=4,column=2) 
education_chosen.current() 
Label(window,text="Resume:",font="Helvetica 14").grid(row=5,column=1)
def UploadAction(event=None):
    path = filedialog.askopenfilename(filetypes =[('PDF Files', '.pdf'),('DOC Files','.docx')])
    if path: 
        filename = os.path.basename(path)
        Label(window,text="Selected File is: ", font="Helvetica 12",fg="red").grid(row=5,column=3)
        Label(window,text=filename, font="Helvetica 12",fg="black").place(x=850,y=215)
    else:
        Label(window,text="File Not Selected!", font="Helvetica 14",fg="red").grid(row=5,column=3)

button = tk.Button(window, text='Upload File',width=34,command=UploadAction).grid(row=5,column=2)
Label(window,text="Address: ",font="Helvetica 14").grid(row=6,column=1)

text4 = Entry(window,width=40)
text4.insert(0,'Address 1')
text4.grid(row=6,column=2)

text5 = Entry(window,width=40)
text5.insert(0,'Address 2')
text5.grid(row=7,column=2)

dropdown2 = tk.StringVar(value="Select a Country") 
country_chosen = ttk.Combobox(window,width=35,textvariable=dropdown2,state="readonly") 
  
# Adding combobox drop down list 
country_chosen['values'] = (' India',  
                          ' UK', 
                          ' USA', 
                          " CANADA", 
                          " Germany", 
                          ' Austria') 
country_chosen.grid(row=8,column=2,pady=(5,0)) 
country_chosen.current()

text6 = Entry(window,width=40)
text6.insert(0,'CITY')
text6.grid(row=9,column=2)

text7 = Entry(window,width=40)
text7.insert(0,'STATE')
text7.grid(row=9,column=3,padx=(1,0))

text8 = Entry(window,width=40)
text8.insert(0,'ZIP CODE')
text8.grid(row=9,column=4,padx=(1,0))

Label(window,text="Phone Number: ",font="Helvetica 14").grid(row=10,column=1)
text9 = Entry(window,width=15).grid(row=10,column=2,padx=(0,150))
text10 = Entry(window,width=30).grid(row=10,column=2)

Label(window,text="What are your hobbies?",font="Helvetica 14").grid(row=11,column=1)
text11 = Entry(window,width=40).grid(row=11,column=2)

Label(window,text="Precious/Current Employment Details", font="Helvetica 16 bold",fg="red").grid(row=12,column=1,pady=(20,0))

Label(window,text="Company Name: ",font="Helvetica 14").grid(row=13,column=1)
text12 = Entry(window,width=40).grid(row=13,column=2)

Label(window,text="Job Title: ",font="Helvetica 14").grid(row=14,column=1)
text13 = Entry(window,width=40).grid(row=14,column=2)

Label(window,text="How long were you here?: ",font="Helvetica 14").grid(row=15,column=1)
text14 = Entry(window,width=40).grid(row=15,column=2)


Label(window,text="Reference #1", font="Helvetica 14 bold",fg="red").grid(row=16,column=1,pady=(10,0))

Label(window,text="Name: ",font="Helvetica 14").grid(row=17,column=1)
text15 = Entry(window,width=40).grid(row=17,column=2)

Label(window,text="Phone: ",font="Helvetica 14").grid(row=18,column=1)
text16 = Entry(window,width=40).grid(row=18,column=2)

Label(window,text="Reference #2", font="Helvetica 14 bold",fg="red").grid(row=19,column=1,pady=(10,0))

Label(window,text="Name: ",font="Helvetica 14").grid(row=20,column=1)
text17 = Entry(window,width=40).grid(row=20,column=2)

Label(window,text="Phone: ",font="Helvetica 14").grid(row=21,column=1)
text18 = Entry(window,width=40).grid(row=21,column=2)

button_1 = Button(window, text="SUBMIT", padx=10, pady=5, bg="black", fg="white").place(relx=0.5, rely=0.89, anchor=CENTER)


window.mainloop()
