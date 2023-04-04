from random import *
import mysql.connector as mydb

mycon = mydb.connect(host='localhost',user='root',password="",database="company")
mycur = mycon.cursor()

s=("Marlo Ramaswamy,Yashraj Gandhi,Arjun Bose,Rakhi Thakkar,Bimla Bandi,Prabha Mehta,Nilima Amin,Zara Palan,Jagdish Divan,Ibrahim Chacko")
l=s.split(",")

for i in range(1,11):
  x=randint(20,35)*1000
  k=randint(0,2)
  d=["PYTHON","MYSQL","TKINTER"]
  y=d[k]
  print(x,y)
  n=l[i-1]
  mycur.execute("insert into emp values("+ str(i) +",'"+ n +"','"+ y +"',"+ str(x) +")")
  mycur.execute("commit")


    
  
