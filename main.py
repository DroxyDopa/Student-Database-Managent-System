import mysql.connector
username=input("Enter your mysql user name: ")
pwd=input('Enter your mysql password: ')
mydb=mysql.connector.connect(
    host='localhost',
    user=username,
    passwd=pwd,
    database='students')



#FUNCTION TO ADD STUDENT'S RESULT
mycursor=mydb.cursor()
addResultForm="insert into result values(%s,'%s','%s',%s)"
def addResult():
        num=input("Enter student number: ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
        numlist=[]
        mycursor.execute('select snum from result')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        num=input('Student number already exists in database. Enter another valid number: ')
        snum=int(num)
        name=input("Enter student name: ")

        stream=input("Enter student stream: ")
        while stream not in ['SCIENCE','HUMANITIES','science','ARTS','COMMERCE','Science','humanities','commerce','arts','Humanities','Arts','Commerce']:
                stream=input("Enter a valid stream (Commerce,Humanities,Science): ")
             
        marks_average=float(input("Enter avg marks: "))
        while marks_average<0 or marks_average>100:
                marks_average=float(input("Enter valid average marks: "))
                
        student=(snum,name,stream,marks_average)
        mycursor.execute(addResultForm %student)
        mydb.commit()
        print('Student details successfully added.')
        print('**********************************')



#FUNCTION TO ADD STUDENT'S CONTACT INFORMATION      
addContactForm="insert into contactinfo values(%s,'%s','%s','%s',%s,%s,'%s')"
def addContact():
        num=input("Enter student number: ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
        numlist=[]
        mycursor.execute('select snum from contactinfo')
        for x in mycursor:
                numlist+=x
                while int(num) in numlist:
                        while len(num)!=4 or num.isnumeric()==False:
                                num=input('Student number already exists in database. Enter another valid number: ')
        snum=int(num)
        mycursor.execute('select snum from result')
        result_numlist=[]
        for x in mycursor:
                result_numlist+=x
        if snum in result_numlist:
                mycursor.execute('select name from result where snum=(%s);' %(snum))
                row=mycursor.fetchone()
                tempname=row[0]
                name=input("Enter student's name")
                while name!=tempname:
                        print("Entered student name does not match existing student's name whose roll number is ",snum," and name is ",tempname)
        else:
                name=input("Enter student's name")
        father_name=input("Enter Student's Father's name: ")
        mother_name=input("Enter Student's Mother's name: ")
        contact1=int(input("Enter primary contact number: "))
        contact2=int(input("Enter secondary contact number: "))
        address=input("Enter student's address: ")

                  
        student=(snum,name,father_name,mother_name,contact1,contact2,address)
        mycursor.execute(addContactForm %student)
        mydb.commit()
        print('Student details successfully added')
        print('**********************************')



#FUNCTION TO GET STUDENT'S RESULT
getResultForm="select * from result where snum=%s"
def getResult():
        num=input('Enter student number you want result of: ')
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from result')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                        while int(num) not in numlist:
                                num=input('Student result does not exist in database. Enter another valid number: ')
                        snum=int(num)
                        mycursor.execute(getResultForm %snum)
                        row=mycursor.fetchone()
                        snum=row[0]
                        name=row[1]
                        stream=row[2]
                        marks_average=row[3]
                        print("Student roll:",snum)
                        print("Student's name: ",name)
                        print("Student's stream: ",stream)
                        print("Student's average marks: ", marks_average)
                        print('**********************************')



#FUNCTION TO GET STUDENT'S CONTACT INFORMATION                  
getContactForm="select * from contactinfo where snum=%s"
def getContact():
        num=input('Enter student number you want contact information of: ')
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from contactinfo')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no contact information entries in the database")
                        print("**********************************")
                        
                else:
                        while int(num) not in numlist:
                                num=input('Student contact information does not exist in database. Enter another valid number: ')
                        snum=int(num)
                        mycursor.execute(getContactForm %snum)
                        row=mycursor.fetchone()
                        snum=row[0]
                        name=row[1]
                        father_name=row[2]
                        mother_name=row[3]
                        contact1=row[4]
                        contact2=row[5]
                        address=row[6]
                        print("Student's roll:",snum)
                        print("Student's name: ",name)
                        print("Student's father's name : ",father_name)
                        print("Student's mother's name: ",mother_name)
                        print("Primary contact number: ",contact1)
                        print("Secondary contact number: ",contact2)
                        print("Student's address: ",contact2)
                        print('**********************************')



#FUNCTION TO MODIFY STUDENT'S RESULT
def modifyResult():
        num=input("Enter student number: ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
                
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from result')
                for x in mycursor:
                        numlist+=x
        while int(num) not in numlist:
                print("There is no pre-existing entry for ",int(num)," in the results table")
                num=input("Enter another roll number: ")
        snum=int(num)
        name=input("Enter student name: ")
        

        stream=input("Enter student stream: ")
        while stream not in ['SCIENCE','HUMANITIES','science','ARTS','COMMERCE','Science','humanities','commerce','arts','Humanities','Arts','Commerce']:
                stream=input("Enter a valid stream (Commerce,Humanities,Science): ")
             
        marks_average=float(input("Enter avg marks: "))
        while marks_average<0 or marks_average>100:
                marks_average=float(input("Enter valid average marks: "))
                
        student=(snum,name,stream,marks_average)
        mycursor.execute("update result set snum = %s, name = '%s', stream = '%s', marks_average=%s where snum=%s;" %(snum,name,stream,marks_average,snum))
        print("Result Modified Successfully")
        print("**********************************")



#FUNCTION TO MODIFY STUDENT'S CONTACT INFORMATION
def modifyContact():
        num=input("Enter student number: ")
        while len(num)!=4 or num.isnumeric()==False:
                num=input("Enter a valid 4 digit student number: ")
                
        snum=int(num)
        name=input("Enter student's name: ")
        father_name=input("Enter Student's Father's name: ")
        mother_name=input("Enter Student's Mother's name: ")
        contact1=int(input("Enter primary contact number: "))
        contact2=int(input("Enter secondary contact number: "))
        address=input("Enter student's address: ")
        
        mycursor.execute("update contactinfo set snum = %s, name = '%s', father_name = '%s', mother_name='%s', contact1=%s, contact2=%s, address='%s' where snum=%s;" %(snum,name,father_name,mother_name,contact1,contact2,address,snum))
        print("Result Modified Successfully")
        print("**********************************")



#FUNCTION TO DELETE STUDENT'S RESULT
def deleteResult():
        num=input('Enter student number whose result you want to delete: ')
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from result')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no result entries in the database")
                        print("**********************************")
                        
                else:
                        while int(num) not in numlist:
                                num=input('Student result does not exist in database. Enter another valid roll number: ')
                        mycursor.execute("delete from result where snum=(%s);" %(num))
                        print("Result Deleted Successfully")
                        print("**********************************")



#FUNCTION TO DELETE STUDENT'S CONTACT INFORMATION
def deleteContact():
        num=input('Enter student number whose contact information you want to delete: ')
        if len(num)==4:
                numlist=[]
                mycursor.execute('select snum from contactinfo')
                for x in mycursor:
                        numlist+=x
                if len(numlist)==0:
                        print("There are no contact information entries in the database")
                        print("**********************************")
                        
                else:
                        while int(num) not in numlist:
                                num=input('Student contact information does not exist in database. Enter another valid roll number: ')
                        mycursor.execute("delete from contactinfo where snum=(%s);" %(num))
                        print("Result Deleted Successfully")
                        print("**********************************")




while True:
        print("What do you want to do?")
        print("1. Add a Student's result")
        print("2. Add a Student's contact information")
        print("3. Get a Student's result")
        print("4. Get a Student's contact information")
        print("5. Modify a Student's result")
        print("6. Modify a Student's contact information")
        print("7. Delete a Student's result")
        print("8. Delete a Student's contact information")
        print("9 Exit")
        x=input("Enter the number correlating to your choice: ")
        if x=='1':
                addResult()
        elif x=='2':
                addContact()
        elif x=='3':
                getResult()
        elif x=='4':
                getContact()
        elif x=='5':
                modifyResult()
        elif x=='6':
                modifyContact()
        elif x=='7':
                deleteResult()
        elif x=='8':
                deleteContact()
        elif x=='9':
                break
        else:
                print("Please enter a number between 1 and 5")
        print("\n\n\n")
