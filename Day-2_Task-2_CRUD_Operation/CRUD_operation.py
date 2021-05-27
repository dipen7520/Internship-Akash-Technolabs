import mysql.connector
mysqldb=mysql.connector.connect(host='localhost',user='root',password="root")
mycursor = mysqldb.cursor()
try:
    mycursor.execute('create database demo')
except:
    print('DB already exists')
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="demo")
mycursor = mysqldb.cursor()
try:
    mycursor.execute("create table student(id INT,name VARCHAR(255), marks INT)")
except:
    print('table already exists')
print('choose option')
print('1.insert data')
print('2.read data')
print('3.update data')
print('4.delete data')
 
option = int(input('enter your choice:'))
if option ==1:
    print("-----We are inserting data-----")
    name = input("enter name:")
    marks = input("enter marks:")
    ins_str = "insert into student(name,marks) values('{}',{});".format(name,marks)
    print(ins_str)
    try:
        mycursor.execute(ins_str)
        mysqldb.commit()
    except:
        mysqldb.rollback()
    mysqldb.close()
elif option == 2:
    print('-----retrive data-----')
    try:
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        print("id","name","marks")
        for i in data:
            print(i[0],i[1],i[2])
    except:
        print("failed to get data from DB")    
elif option == 3:
    print("-----Update Data------") 
    id = int(input('enter student id to update'))
    print("select option for update")
    print("1.update only name")
    print("2.update only marks")
    print("3.update both")
    op = input("enter update option:")
    if op == "1":
        print("----update only name---")
        try:                
            name = input("enter new name :")
            update = "UPDATE student SET name='{}' WHERE id={}".format(name,id)
            mycursor.execute(update)
            mysqldb.commit()
        except:
            print("failed to update data from DB")
    elif op == "2":
        try:
            print("----update only marks---")   
            marks = int(input("enter new marks :"))
            update = "UPDATE student SET marks={} WHERE id={}".format(marks,id)
            mycursor.execute(update)
            mysqldb.commit()
        except:
            print("failed to update data from DB")
    elif op == "3":
        try:
            print("----update both---")   
            name = input("enter new name:")
            marks = int(input("enter new marks :"))
            update = "UPDATE student SET name='{}',marks={} WHERE id={}".format(name,marks,id)
            mycursor.execute(update)
            mysqldb.commit()
        except:
            print("failed to update data from DB")
elif option== 4:
    id = input('Enter ID to be Deleted')
    try:
        mycursor.execute("DELETE FROM student WHERE id={}".format(id)) 
        mysqldb.commit()
    except:
        mysqldb.rollback()
    mysqldb.close()