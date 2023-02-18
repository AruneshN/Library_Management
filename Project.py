from tkinter import*
from tkinter import messagebox
from functools import partial
from tkinter import ttk
import pymysql
import subprocess as sp

db_connection=pymysql.connect(
    host="localhost",
    user="root",
    password="Preetha@27",
    database="library"
)
my_database=db_connection.cursor()
print("connected successfully...")

root=Tk()
root.title("FORM")
root.geometry("1200x1200")
def main():
    
    f1=Frame(root,bg="#753c72",height=1200,width=1200)
    f1.pack(fill=X)  
    label=Label(f1,text="LIBRARY MANAGEMENT SYSTEM",height="2",width="40",bd=4,font="Calibri 30 bold",fg='black')
    label.place(x=400,y=130)
    
    def register():
        f3=Frame(f1,bg="grey",height=1200)
        f3.pack(fill=X)
        
        label=Label(f3,text="CREATE NEW ACCOUNT",width=20,font=("Algerian", 20),bg="black",fg="white")
        label.place(x=650,y=30)
        label1=Label(f3,text="USERNAME")
        label1.place(x=620,y=90)
        label2=Label(f3,text="PASSWORD")
        label2.place(x=620,y=130)
        label3=Label(f3,text="CONFIRM PASSWORD")
        label3.place(x=565,y=170)

        def d(ed1,ed2,ed3):
            Username=e1.get()
            Password=e2.get()
            Confirmpassword=e3.get()
            sql_statement="INSERT INTO entry(Username,Password,Confirmpassword)values(%s,%s,%s)"
            values=(Username,Password,Confirmpassword)
            my_database.execute(sql_statement,values)
            db_connection.commit()
            print("Success")
            
            if(e2.get() and e3.get() and e2.get()==e3.get()):
                messagebox.showinfo("showinfo","Registered Successfully")
            else:
                messagebox.showerror("showerror","fields can't be empty")
        
        e1=Entry(f3,bd=4,width='40')   
        e1.place(x=710,y=90)
        ed1=StringVar()
        
        e2=Entry(f3,bd=4,show="*",width='40')
        e2.place(x=710,y=130)
        ed2=IntVar()
        
        e3=Entry(f3,bd=4,show="*",width='40')
        e3.place(x=710,y=170)
        ed3=IntVar()
                               
        d=partial(d,ed1,ed2,ed3)
        Button(f3,text="SUBMIT",bg='red',fg='white',command=d).place(x=770,y=230)
        Button(f3,text='BACK',bg='red',fg='white',command=f3.destroy).place(x=840,y=230)

    def login():
        
        f2=Frame(f1,bg="#63b2d4",height=1200,width=1200)
        f2.pack(fill=X)
        
        label=Label(f2,text="USER LOGIN",width=20,font=("Algerian", 20),bg="black",fg="white")
        label.place(x=650,y=30)
        label1=Label(f2,text="USERNAME")
        label1.place(x=650,y=100)
        label2=Label(f2,text="PASSWORD")
        label2.place(x=650,y=140)

        def f():
            username=e1.get()
            password=e2.get()
            
            sql="select*from entry where Username=%s and Password = %s"
            
            my_database.execute(sql,[(username),(password)])
            res=my_database.fetchall()
            print(res)
            if(res):
                f4=Frame(f2,height="1600",width="1600",bg="lightblue")
                f4.pack()
                label=Label(f4,text="Choose your Authors",width=20,font=("Algerian", 20),bg="black",fg="white")
                label.place(x=640,y=30)

                author=ttk.Combobox(f4,values=["J.K Rowling","William Shakespeare","Charles Dickens","James Joyce","Leo Tolstoy"],font='60')
                author.place(x=700, y=150)
                def g():
                    if(author.get()=="J.K Rowling"):
                        messagebox.showinfo("info","success")
                        f5=Frame(f4,height="1600",width="1600",bg="#ffcccc")
                        f5.pack()
                        label=Label(f5,text="Books Written by J.K.Rowling",font=("Algerian", 20),bg="white",fg="black")
                        label.place(x=590,y=100)
                        
                        a=ttk.Combobox(f5,width="35",font=("Arial",12),values=["Harry Potter and the Sorcerer’s Stone","Quidditch Through the Ages"])
                        a.place(x=630,y=220)
                        def p():
                            if(a.get()=="Harry Potter and the Sorcerer’s Stone"):
                                programname="notepad.exe"
                                filename='jk.txt'
                                sp.Popen([programname,filename])
                            elif(a.get()=="Quidditch Through the Ages"):
                                programname="notepad.exe"
                                filename='Quidditch.txt'
                                sp.Popen([programname,filename])        
                            
                        Button0=Button(f5,text="SUBMIT",fg='black',height="1",width="20",bd=4,command=p)
                        Button0.place(x=730,y=310)
                        Button1=Button(f5,text="BACK",fg='black',height="1",width="20",bd=4,command=f5.destroy)
                        Button1.place(x=730,y=370)
                
                    elif(author.get()=="William Shakespeare"):
                            f6=Frame(f4,height="1600",width="1600",bg="#b3d9ff")
                            f6.pack()
                            label=Label(f6,text="Books Written by William Shakespeare",font=("Algerian", 20),bg="white",fg="black")
                            label.place(x=540,y=130)

                            a=ttk.Combobox(f6,width="35",font=("Arial",12),values=["Hamlet","Richard III"])
                            a.place(x=640,y=220)

                            def q():
                                if(a.get()=="Hamlet"):
                                    programname="notepad.exe"
                                    filename='Hamlet.txt'
                                    sp.Popen([programname,filename])
                                elif(a.get()=="Richard III"):
                                    programname="notepad.exe"
                                    filename='Richard.txt'
                                    sp.Popen([programname,filename])
                                 
                            
                            Button1=Button(f6,text="SUBMIT",fg='black',height="1",width="20",bd=4,command=q)
                            Button1.place(x=730,y=310)
                            Button2=Button(f6,text="BACK",fg='black',height="1",width="20",bd=4,command=f6.destroy)
                            Button2.place(x=730,y=370)
                        
                    elif(author.get()=="Charles Dickens"):
                        f7=Frame(f4,height="1600",width="1600",bg="lightgreen")
                        f7.pack()
                        label=Label(f7,text="Books Written by Charles Dickens",font=("Algerian", 20),bg="white",fg="black")
                        label.place(x=560,y=130)

                        a=ttk.Combobox(f7,width="35",font=("Arial",12),values=["The Pickwick Papers","Oliver Twist"])
                        a.place(x=640,y=220)

                        def r():
                            if(a.get()=="The Pickwick Papers"):
                                programname="notepad.exe"
                                filename='Pickwick.txt'
                                sp.Popen([programname,filename])
                            elif(a.get()=="Oliver Twist"):
                                programname="notepad.exe"
                                filename='oliver.txt'
                                sp.Popen([programname,filename])
                                 
                            
                        Button3=Button(f7,text="SUBMIT",fg='black',height="1",width="20",bd=4,command=r)
                        Button3.place(x=730,y=310)
                        Button4=Button(f7,text="BACK",fg='black',height="1",width="20",bd=4,command=f7.destroy)
                        Button4.place(x=730,y=370)
                        
                    elif(author.get()=="James Joyce"):
                        f8=Frame(f4,height="1600",width="1600",bg="#ffcce6")
                        f8.pack()
                        label=Label(f8,text="Books Written by James Joyce",font=("Algerian", 20),bg="white",fg="black")
                        label.place(x=580,y=130)

                        a=ttk.Combobox(f8,width="35",font=("Arial",12),values=["Dubliners","A Portrait of the Artist as a Young Man"])
                        a.place(x=640,y=220)

                        def s():
                            if(a.get()=="Dubliners"):
                                programname="notepad.exe"
                                filename='dubliners.txt'
                                sp.Popen([programname,filename])
                            elif(a.get()=="A Portrait of the Artist as a Young Man"):
                                programname="notepad.exe"
                                filename='Portrait.txt'
                                sp.Popen([programname,filename])
                                 
                            
                        Button4=Button(f8,text="SUBMIT",fg='black',height="1",width="20",bd=4,command=s)
                        Button4.place(x=730,y=310)
                        Button5=Button(f8,text="BACK",fg='black',height="1",width="20",bd=4,command=f8.destroy)
                        Button5.place(x=730,y=370)
                        
                    elif(author.get()=="Leo Tolstoy"):
                        f9=Frame(f4,height="1600",width="1600",bg="#ffd9b3")
                        f9.pack()
                        label=Label(f9,text="Books Written by Leo Tolstoy",font=("Algerian", 20),bg="white",fg="black")
                        label.place(x=590,y=130)
                        
                        a=ttk.Combobox(f9,width="35",font=("Arial",12),values=["War and Peace","Anna Karenina"])
                        a.place(x=640,y=220)
                        def t():
                            if(a.get()=="War and Peace"):
                                programname="notepad.exe"
                                filename='war.txt'
                                sp.Popen([programname,filename])
                            elif(a.get()=="Anna Karenina"):
                                programname="notepad.exe"
                                filename='Karenina.txt'
                                sp.Popen([programname,filename])
                                 
                            
                        Button5=Button(f9,text="SUBMIT",fg='black',height="1",width="20",bd=4,command=t)
                        Button5.place(x=730,y=310)
                        Button6=Button(f9,text="BACK",fg='black',height="1",width="20",bd=4,command=f9.destroy)
                        Button6.place(x=730,y=370)
                        
                    else:
                        messagebox.showwarning("Warning","Choose within the options")
                    
                
                Button1=Button(f4,text="SUBMIT",fg='black',height="1",width="25",bd=3,command=g)
                Button1.place(x=730,y=290)
    
                Button2=Button(f4,text="EXIT",fg='black',height="1",width="25",bd=3,command=f2.destroy)
                Button2.place(x=730,y=370)

                
            else:
                messagebox.showinfo("warning","No User Found")
                
        e1=Entry(f2,bd=4,width='40')
        e1.place(x=740,y=100)
        eb1=StringVar()
        
        e2=Entry(f2,bd=4,show="*",width='40')
        e2.place(x=740,y=140)
        eb2=StringVar()
    
        
        Button(f2,text='LOGIN',bg='black',fg='white',command=f).place(x=770,y=200)
        Button(f2,text='BACK',bg='black',fg='white',command=f2.destroy).place(x=840,y=200)
        
        
  #main  
    Button1=Button(f1,text="Login",fg='black',height="2",width="30",bd=4,command=login)
    Button1.place(x=700,y=350)
    
    Button2=Button(f1,text="Register",fg='black',height="2",width="30",bd=4,command=register)
    Button2.place(x=700,y=420)


main()
