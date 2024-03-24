#Initializing Variables
addNew='new'
command=0
redo=1

#importing packages
import mysql.connector
import functions
#open database connection with a dictionary

conDict={'host':'localhost',
         'database':'doc334_icw',
         'user':'root','password':''}
db=mysql.connector.connect(**conDict)

#prepare a cursor object 
cursor=db.cursor()

while(redo==1):  #looping the entire program
    print("Task Keys :\nAdd=1\nSearch=2\nUpdate=3\nDelete=4\nRead/Write Chapters=5\nRestore Databse=6\n")
    while True:  #error handling
        try:
            command=int(input("Enter the task key :"))
            print()
            break
        except:
            print("invalid input")
    
    if(command==1):   #Task : Insert
        functions.insert(addNew,db,cursor)
    elif(command==2): #Task : Search
        functions.search(cursor)

    elif(command==3):  #Task : Update
        functions.update(cursor,db)

    elif(command==4):  #Task : Delete
        functions.delete(cursor,db)
        
    elif(command==5):  #Task :Chapter Handling
        functions.chapter(cursor)
        
    elif(command==6):  #Task :Restore Database  #For marking purposes
        print("You are about to restore the database ")
        code=int(input("Type 1021 to proceed :")) #confirmation
        if(code==1021):
            cursor.execute("DELETE FROM subject")
            db.commit()
            cursor.execute("DELETE FROM book")
            db.commit()
            cursor.execute("DELETE FROM chapter")
            db.commit()
            print("The database has been restored")
        else:
            print("invalid code")
    else:
        print("invalid input")
    print()
    redo=int(input("Type 1 to rerun the program or Type any other number to exit :")) #rerun the program or not
    print()
print("--Thank you for using the ABC Book Manager.--") #end

#disconnect from database
db.close()
