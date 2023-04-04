from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import mysql.connector as mydb
import csv

#connecting to database "company" 
mycon = mydb.connect(host="localhost",user="root",password="",database="company")
mycur = mycon.cursor() #creating a cursor object


def insert(): #function to add record to table

  global mycon
  global mycur

  #assigning variable to values entered in entries
  empno=e_empno.get()
  name=e_name.get()
  department=e_department.get()
  salary=e_salary.get()
  post=e_post.get()

  try:
    #to check if empno coincides with existing empno
    mycur.execute("select * from emp where empno="+ empno)
    data=mycur.fetchone()

    if empno=="" or name=="" or department=="" or salary=="" or post=="":
      #if any one entry is not filled following will be shown
      msgbox.showinfo("Insert Status","All fields required")
      
    elif (data)!=None: #if empno coincides shows error
      msgbox.showerror("Insert Status","Entry already exists by the Emp No: "+empno)
      
    else:
      #query to insert record to table
      mycur.execute("insert into emp values("+ empno +",'"+ name +"','"+ department +"',"+ salary +",'"+ post +"')")
      mycon.commit() # commiting current transactions with SQL database
      
      msgbox.showinfo("Insert Status","Inserted successfully") #feedback
      refresh()
  except:
    msgbox.showerror("Insert Status","Invalid Entries") #feedback 


def update(): #function to update record to table
  global mycon
  global mycur

  #assigning variable to values entered in entries
  empno=e_empno.get()
  name=e_name.get()
  department=e_department.get()
  salary=e_salary.get()
  post=e_post.get()

  try:
    #to check if empno coincides with existing empno
    mycur.execute("select * from emp where empno="+ empno)
    data=mycur.fetchone()
    
    if empno=="" or name=="" or department=="" or salary=="" or post=="":
      #if any one entry is not filled following will be shown
      msgbox.showinfo("Update Status","All fields required")
      
    elif data==None:
      #if empno doesn't coincides shows error
      msgbox.showerror("Update Status","Entry does not exist by the Emp No: "+empno)
      
    else:
      #query to update record in table
      mycur.execute("update emp set name='"+ name +"',department='"+ department +"',salary="+ salary +",post='"+ post +"'where empno="+ empno)
      mycon.commit() # commiting current transactions with SQL database 

      refresh()
    
      msgbox.showinfo("Update Status","Updated successfully") #feedback
  except:
    msgbox.showerror("Update Status","Invalid Entries") #feedback 

def delete():
  global mycon
  global mycur

  #reading the entry
  empno=e_empno.get()

  try:
    #to check if empno coincides with existing empno
    mycur.execute("select * from emp where empno="+ empno)
    data=mycur.fetchone()
      
    if empno=="":
      msgbox.showinfo("Delete Status","Employee No. required")
    elif data==None: #if empno coincides shows error
        msgbox.showerror("Delete Status","Entry doesn't exists by the Emp No: "+empno)
    else:
      
      res=msgbox.askquestion("Delete", "Are You Sure?", icon='warning') #feedback
      if res=='yes':
        #query to delete record from table
        mycur.execute("delete from emp where empno="+ empno)
        mycon.commit() # commiting current transactions with SQL database
        msgbox.showinfo("Delete Status","Deleted successfully") #feedback
        clear()
      show()
  except:
    msgbox.showerror("Delete Status","Invalid Entries") #feedback
  
def search():
  global mycon
  global mycur

  #reading the entry
  empno=e_empno.get()
  try:
    mycur.execute("select * from emp where empno="+ empno)
    data=mycur.fetchone()

    #executes code if required entry given
    if empno=="":
      msgbox.showinfo("Search Status","Employee ID required") #feedback
    elif data==None: #if empno coincides shows error
          msgbox.showerror("Search Status","Entry doesn't exists by the Emp No: "+empno)
    else:
      #query to select particular record from table
      mycur.execute("select * from emp where empno ="+ empno)
      clear()
      
      d=mycur.fetchone()

      #inserting record in enteries
      e_empno.insert(0,d[0])
      e_name.insert(0,d[1])
      e_department.insert(0,d[2])
      e_salary.insert(0,d[3])
      e_post.insert(0,d[4])
      
  except:
    msgbox.showerror("Search Status","Invalid Entries") #feedback

def searchByName():
  global mycon
  global mycur

  #reading the entry
  name=e_name.get()

  #executes code if required entry given
  if name=="":
    msgbox.showinfo("Search Status","Name required") #feedback
  else:
    #query to select particular data from SQL database
    mycur.execute("select * from emp where name='"+ name +"'order by empno")
    rows=mycur.fetchall()
    table2.delete(*table2.get_children())
    for row in rows:
      table2.insert('', 'end', text="1", values=row)
    
def searchByDepartment():
  global mycon
  global mycur

  #reading the entry
  department=e_department.get()

  #executes code if required entry given
  if department=="":
    msgbox.showinfo("Search Status","Department required") #feedback
  else:
    #query to select particular data from SQL database
    mycur.execute("select * from emp where department='"+ department +"'order by empno")
    rows=mycur.fetchall()
    table2.delete(*table2.get_children())
    for row in rows:
      table2.insert('', 'end', text="1", values=row)
  return rows

def searchBySalary():
  global mycon
  global mycur

  #reading the entry
  salary=e_salary.get()

  #executes code if required entry given
  if salary=="":
    msgbox.showinfo("Search Status","Salary required") #feedback
  else:
    try:
      #query to select particular data from SQL database
      mycur.execute("select * from emp where salary="+ salary +" order by empno")
      rows=mycur.fetchall()
      table2.delete(*table2.get_children())
      for row in rows:
        table2.insert('', 'end', text="1", values=row)
      return rows
    except:
      msgbox.showerror("Search Status","Invalid Entries") #feedback

def searchByPost():
  global mycon
  global mycur

  #reading the entry
  post=e_post.get()

  #executes code if required entry given
  if post=="":
    msgbox.showinfo("Search Status","Post required") #feedback
  else:
    #query to select particular data from SQL database
    mycur.execute("select * from emp where post='"+ post +"'order by empno")
    rows=mycur.fetchall()
    table2.delete(*table2.get_children())
    for row in rows:
      table2.insert('', 'end', text="1", values=row)
    return rows
    
  mycon.close() #closing connecting to database

def show():
  global mycon
  global mycur

  #query to select all data in order from SQL database
  mycur.execute("select * from emp order by empno")
  rows=mycur.fetchall()
  table.delete(*table.get_children())
  for row in rows:
    table.insert('','end', values=row)

def paySlip():
  global mycon
  global mycur

  #reading the entry
  empno=e_empno.get()

  #executes code if required entry given
  if empno=="":
    msgbox.showinfo("Pay slip Status","Employee No required") #feedback
  else:
    try:
      #query to select particular data from SQL database
      mycur.execute("select * from emp where empno="+ empno)
      data=mycur.fetchone()

      #secondary window
      win = Toplevel(root)
      win.geometry("400x300")
      win.title("Employee Salary")
      
      #labels for text
      emp= Label(win,text="Employee No",font=("bold",10)).place(x=20,y=30)
      emp1=Label(win,text=empno,font=("bold",10)).place(x=200,y=30) #display's EMP ID
      
      name= Label(win,text="Employee Name",font=("bold",10)).place(x=20,y=60)
      name1=Label(win,text=data[1],font=("bold",10)).place(x=200,y=60) #display's Employee Name 
      
      dept= Label(win,text="Employee Department",font=("bold",10)).place(x=20,y=90)
      dept1=Label(win,text=data[2],font=("bold",10)).place(x=200,y=90) #display's Employee Department
      
      post= Label(win,text="Employee Post",font=("bold",10)).place(x=20,y=120)
      post1=Label(win,text=data[4],font=("bold",10)).place(x=200,y=120) #display's Employee Post
      
      sal= Label(win,text="Employee Salary",font=("bold",10)).place(x=20,y=150)
      sal1= Label(win,text=data[3],font=("bold",10)).place(x=200,y=150) #display's Employee Salary
      
      tax=Label(win,text="Tax (10%)",font=("bold",10)).place(x=20,y=180)
      tax1=Label(win,text=int(data[3]*0.1),font=("bold",10)).place(x=200,y=180) #display's Tax on Salary
      
      net=Label(win,text="Net Salary",font=("bold",10)).place(x=20,y=210)
      net1=Label(win,text=int(data[3]*0.9),font=("bold",10)).place(x=200,y=210) #display's Net Salary

      clear()
    except:
      msgbox.showerror("Print Status","Entry doesn't exists") #feedback

def export():
  global mycon
  global mycur

  #reading the entry
  fname=e_name.get()

  #executes code if required entry given
  if fname=="":
    msgbox.showinfo("Export Status","File Name required") #feedback
  else:
    #query to select all data from SQL database
    mycur.execute("select * from emp order by empno")
    data=mycur.fetchall()
    with open(fname +".csv","w",newline="") as f:
      w=csv.writer(f,delimiter=",")
      w.writerow(["EMP ID","NAME","DEPARTMENT","SALARY","POST"])
      w.writerows(data)
    msgbox.showinfo("Export Status","Exported as "+ fname +".csv") #feedback
    refresh()

def exportDepartment():
  global mycon
  global mycur

  #reading the entry
  fname=e_name.get()

  #executes code if required entry given
  if fname=="":
    msgbox.showinfo("Export Status","File Name required") #feedback
  else:
    data=searchByDepartment()
    with open(fname +".csv","w",newline="") as f:
      w=csv.writer(f,delimiter=",")
      w.writerow(["EMP ID","NAME","DEPARTMENT","SALARY","POST"])
      w.writerows(data)
    msgbox.showinfo("Export Status","Exported as "+ fname +".csv") #feedback
    clear()

def exportSalary():
  global mycon
  global mycur

  #reading the entry
  fname=e_name.get()

  #executes code if required entry given
  if fname=="":
    msgbox.showinfo("Export Status","File Name required") #feedback
  else:
    data=searchBySalary()
    with open(fname +".csv","w",newline="") as f:
      w=csv.writer(f,delimiter=",")
      w.writerow(["EMP ID","NAME","DEPARTMENT","SALARY","POST"])
      w.writerows(data)
    msgbox.showinfo("Export Status","Exported as "+ fname +".csv") #feedback
    clear()
    
def exportPost():
  global mycon
  global mycur

  #reading the entry
  fname=e_name.get()

  #executes code if required entry given
  if fname=="":
    msgbox.showinfo("Export Status","File Name required") #feedback
  else:
    data=searchByPost()
    with open(fname +".csv","w",newline="") as f:
      w=csv.writer(f,delimiter=",")
      w.writerow(["EMP ID","NAME","DEPARTMENT","SALARY","POST"])
      w.writerows(data)
    msgbox.showinfo("Export Status","Exported as "+ fname +".csv") #feedback
    clear()
    
def helpme():
  fact="""Employee Database

First table shows all record
Second table only shows requested record only

Enter values to corresponding entries
Entry No 1 : For Employee No
Entry No 2 : For Employee Name or File Name for exporting data
Entry No 3 : For Employee Department
Entry No 4 : For Employee Salary
Entry No 5 : For Employee Post

Press the buttons given below to perform there respective function
Insert-To add employee data to SQL databse
Update-To change employee data in SQL database
Delete-To remove employee Data from SQL database
Search-To search employee Data from SQL database

Menubar has three section File Search and Export
Options for Refreshing,Generating Pay Slip, Help and Exit
Search is for searching multiple records by
  -name
  -department
  -salary
  -post
Export is for exporting all record or specific records by
  -department
  -salary
  -post
"""
  helpwin=Tk() #creates a window
  helpwin.geometry("425x570") #dimensions of help window
  helpwin.title("Employee Database - Help")

  text=Label(helpwin,text=fact,font=("bold",10),justify=LEFT,bg="#ffffff")
  text.place(x=20,y=20) #postion's label

  ok=Button(helpwin,text=" Ok ",font=("italic",10),bg="#ffffff",command=helpwin.destroy)
  ok.place(x=20,y=523) #postion's button

def clear():

  #clearing the entries
  e_empno.delete(0,'end')
  e_name.delete(0,'end')
  e_department.delete(0,'end')
  e_salary.delete(0,'end')
  e_post.delete(0,'end')

def refresh():
  
  #refresh the tables and entries
  clear()
  show()
  table2.delete(*table2.get_children())

def Exit():
  mycon.close() #closing connecting to database
  root.destroy()
  print("Exited!")

#main window and its properties
root=Tk() #creates main window
root.geometry("1150x560") #dimensions of main window
root.title("Employee Database")


#menubar for additional functions
menubar = Menu(root)

optionmenu = Menu(menubar, tearoff=0)
#perform corresponding functions when clicked
optionmenu.add_command(label="Refresh", command=refresh)
optionmenu.add_command(label="Generate pay slip", command=paySlip)
optionmenu.add_command(label="Help", command=helpme)

optionmenu.add_separator()#divides in two sections

optionmenu.add_command(label="Exit", command=Exit) #quits the program
menubar.add_cascade(label="Options", menu=optionmenu)

searchmenu = Menu(menubar, tearoff=0)
searchmenu.add_command(label="Search by Name", command=searchByName)
searchmenu.add_command(label="Search by Department", command=searchByDepartment)
searchmenu.add_command(label="Search by Salary", command=searchBySalary)
searchmenu.add_command(label="Search by Post", command=searchByPost)
menubar.add_cascade(label="Search", menu=searchmenu)

exportmenu = Menu(menubar, tearoff=0)
exportmenu.add_command(label="Export All", command=export)
exportmenu.add_command(label="Export by Department", command=exportDepartment)
exportmenu.add_command(label="Export by Salary", command=exportSalary)
exportmenu.add_command(label="Export by Post", command=exportPost)
menubar.add_cascade(label="Export", menu=exportmenu)

root.config(menu=menubar)


#labels for text
empno=Label(root,text="Enter Employee No",font=("bold",10))
empno.place(x=20,y=30) #postion's label

name=Label(root,text="Enter Name",font=("bold",10))
name.place(x=20,y=70) #postion's label

department=Label(root,text="Enter Department",font=("bold",10))
department.place(x=20,y=110) #postion's label

salary=Label(root,text="Enter Salary",font=("bold",10))
salary.place(x=20,y=150) #postion's label

post=Label(root,text="Enter Post",font=("bold",10))
post.place(x=20,y=190) #postion's label

#entries to enter data
e_empno=Entry(root)
e_empno.place(x=200,y=30) #postion's entry

e_name=Entry(root)
e_name.place(x=200,y=70) #postion's entry

e_department=Entry(root)
e_department.place(x=200,y=110) #postion's entry

e_salary=Entry(root)
e_salary.place(x=200,y=150) #postion's entry

e_post=Entry(root)
e_post.place(x=200,y=190) #postion's entry


# buttons which perform basic functions
insert=Button(root,text=" Insert ",font=("italic",10),bg="#66ccff",command=insert)
insert.place(x=20,y=250) #postion's button

update=Button(root,text="Update",font=("italic",10),bg="#66ccff",command=update)
update.place(x=100,y=250) #postion's button

delete=Button(root,text="Delete",font=("italic",10),bg="#ff6666",command=delete)
delete.place(x=180,y=250) #postion's button

search=Button(root,text="Search",font=("italic",10),bg="#ffe97a",command=search)
search.place(x=260,y=250) #postion's button

#table to show all data of table emp of SQL database
table=ttk.Treeview(root,column=("c1","c2","c3","c4","c5"),show="headings",height=15)
#column properties
table.column("# 1", anchor=CENTER,width=60)
table.heading("# 1", text="EMP NO")
table.column("# 2", anchor=CENTER)
table.heading("# 2", text="Name")
table.column("# 3", anchor=CENTER)
table.heading("# 3", text="Department")
table.column("# 4", anchor=CENTER,width=100)
table.heading("# 4", text="Salary")
table.column("# 5", anchor=CENTER)
table.heading("# 5", text="Post")
table.place(x=350,y=30) #postion's table in correct place

#table to show specific mass searches from menu
table2=ttk.Treeview(root,column=("c1","c2","c3","c4","c5"),show="headings",height=6)
#column properties
table2.column("# 1", anchor=CENTER,width=60)
table2.heading("# 1", text="EMP NO")
table2.column("# 2", anchor=CENTER)
table2.heading("# 2", text="Name")
table2.column("# 3", anchor=CENTER)
table2.heading("# 3", text="Department")
table2.column("# 4", anchor=CENTER,width=100)
table2.heading("# 4", text="Salary")
table2.column("# 5", anchor=CENTER)
table2.heading("# 5", text="Post")
table2.place(x=350,y=380) #postion's table in correct place

show()

root.mainloop() #executes what we wish to execute in an application
