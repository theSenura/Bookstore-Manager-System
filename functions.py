def search(cursor): #function : search
    "search books, subjects"
    #Initializing variables
    mode=0
    SearchBy=0
    Author=''
    Publisher=''
    BookNo=''
    Titl=''
    
    while True:   #error handling
        try:
            mode=int(input("Type 1 for Wide search or 2 for Filtered search :"))
            break
        except:
            print("invalid input")
    print()

    if(mode==1):  #wide search
        print("Wide search displays all records that consist of the input.\nSupports any data in BookNo,Title,Author or Publisher columns\n")
        Search=input("Search :")
        #have seperate execute queries and print statements for the relevant columns to check for any matches of the user input with the records. 
        #execute sql query 
        cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE BookNo="'+Search+'" ')
        #fetch results 
        data= cursor.fetchall()
        #display records
        for item in data:
            print("Book Number :",item[0])
            print("Book Title : ",item[1])
            print("Author :",item[2])
            print("Publisher :",item[3])
            print("Year Published :",item[4])
            print("Location :",item[5])
            print("Subject Code :",item[6])
            print("Price :",item[7])
            print("ISBN :",item[8])
            print('')

        cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Title="'+Search+'" ')
        data= cursor.fetchall()
        #display records
        for item in data:
            print("Book Number :",item[0])
            print("Book Title : ",item[1])
            print("Author :",item[2])
            print("Publisher :",item[3])
            print("Year Published :",item[4])
            print("Location :",item[5])
            print("Subject Code :",item[6])
            print("Price :",item[7])
            print("ISBN :",item[8])
            print('')

        cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Author="'+Search+'" ')
        data=cursor.fetchall()
        #display records
        for item in data:
            print("Book Number :",item[0])
            print("Book Title : ",item[1])
            print("Author :",item[2])
            print("Publisher :",item[3])
            print("Year Published :",item[4])
            print("Location :",item[5])
            print("Subject Code :",item[6])
            print("Price :",item[7])
            print("ISBN :",item[8])
            print('')

        cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Publisher="'+Search+'" ')
        data=cursor.fetchall()
        #display records    
        for item in data:
            print("Book Number :",item[0])
            print("Book Title : ",item[1])
            print("Author :",item[2])
            print("Publisher :",item[3])
            print("Year Published :",item[4])
            print("Location :",item[5])
            print("Subject Code :",item[6])
            print("Price :",item[7])
            print("ISBN :",item[8])
            print('')

    elif(mode==2):
        print("Keys :\nBookNo=1\nTitle=2\nAuthor=3\nPublisher=4\n") #printing the keys
        while True:  #error handling
            try:
                SearchBy=int(input("Search by BookNo or Title or Author or Publisher :"))
                break
            except:
                print("invalid input")

        if(SearchBy==1):  #Search from book number
            BookNo=input("Enter book number :")
            print()
        #execute sql query 
            cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE BookNo="'+BookNo+'" ')

        #fetch results
            data= cursor.fetchall()
        elif(SearchBy==2): #Search from title
            
            Title=input("Enter the book Title :")
            cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Title="'+Title+'" ')
            data= cursor.fetchall()
            
        elif(SearchBy==3):  #Search from author
            Author=input("Author :")
            cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Author="'+Author+'" ')
            data=cursor.fetchall()
            
        elif(SearchBy==4):  #Search from publisher
            Publisher=input("Publisher :")
            cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE Publisher="'+Publisher+'" ')
            data=cursor.fetchall()

        #display records    
        for item in data:
            print("Book Number :",item[0])
            print("Book Title : ",item[1])
            print("Author :",item[2])
            print("Publisher :",item[3])
            print("Year Published :",item[4])
            print("Location :",item[5])
            print("Subject Code :",item[6])
            print("Price :",item[7])
            print("ISBN :",item[8])
            print('')
    return


def insert(addNew,db,cursor): #function : insert
            "Insert books, subjects or book chapters"
            add=int(input("Type 1 to add a new subject or 2 to enter a new book or 3 to add new book chapters :"))
            #Initializing variables
            BookNo=''
            Title=''
            SubCode=''
            Author=''
            Publisher=''
            YearPub=''
            price=0
            ISBN=''
            Location=''
            addNew='new'
            ChapterNo=0
            ChapterTitle=''
            StartPage=0
            EndPage=0
            if(add==1):
                while(addNew=='new'):
                    SubCode=input("Enter the new subject code:")
                    SubName=input("Enter the subject name :")
            #execute sql query 
                    subDetail="INSERT INTO subject(SubjectCode,SubjectName)VALUES(%s,%s)" #inserting values into subject table
                    subValues=(SubCode,SubName)
                    cursor.execute(subDetail,subValues)
                    db.commit() #comit
                    print(cursor.rowcount,"New subject added. Click enter to exit .")
                    addNew=input("Type 'new' to add a new subject or click Enter to exit :")
                addNew='new'
            elif(add==2):
                while(addNew=='new'):
            #read user input
                    BookNo=input("Enter the book number :")
                    Title=input("Enter the book title :")
                    SubCode=input("Enter the subject code :")
                    Author=input("Enter the author :")
                    Publisher=input("Enter the publisher :")
                    YearPub=int(input("Enter the year published :"))
                    price=int(input("Enter the book price :"))
                    ISBN=input("Enter the ISBN :")
                    Location=input("Enter where the book is located :")
            #execute sql query 
                    BookDetail="INSERT INTO book(BookNo,Title,SubjectCode,Author,Publisher,YearPublished,Price,ISBN,Location)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    Values=(BookNo,Title,SubCode,Author,Publisher,YearPub,price,ISBN,Location) #inserting values into book table
                    cursor.execute(BookDetail,Values)
                    db.commit() #comit
                    print(cursor.rowcount,"New book added")
                    addNew=input("Type 'new' to add a new book or click Enter to exit :")
            if(add==3):
                while(addNew=='new'):
                    BookNo=input("Enter the Book number :")
                    num=int(input("Enter the number of chapters :"))
                    for count in range(0,num):
                        ChapterNo=int(input("Enter the Chapter number :"))
                        ChapterTitle=input("Enter the chapter title :")
                        StartPage=int(input("Enter the chapter starting page :"))
                        EndPage=int(input("Enter the chapter end page :"))
                #execute sql query 
                        ChaptDetail="INSERT INTO chapter(BookNo,ChapterNo,ChapterTitle,StartPage,EndPage)VALUES(%s,%s,%s,%s,%s)" #inserting values into chapter table
                        ChaptValues=(BookNo,ChapterNo,ChapterTitle,StartPage,EndPage)
                        cursor.execute(ChaptDetail,ChaptValues)
                        db.commit() #comit
                        count+=1
                        print(cursor.rowcount,"New chapter added.")
                    addNew=input("Type 'new' to add new book chapters or click Enter to exit :")
                addNew='new'
            return
def update(cursor,db): #function : update
            "Update data in Book, Subject tables"
            #Initialize variables
            BookNo=''
            NewTitle=''
            NewNo=''
            NewSubCode=''
            NewAuthor=''
            NewPub=''
            NewYear=''
            NewISBN=''
            NewLocation=''
            NewSubName=''
            
            #print the keywords
            print("Book table Keys :\nBookNo=1\nTitle=2\nSubjectCode=3\nAuthor=4\nPublisher=5\nYearPublished=6\nPrice=7\nISBN=8\nLocation=9\n")
            print("Subject table Keys :\nSubjectCode=10\nSubjectName=11\n")


            update=0
            #Error handling
            while True:
                try:
                    update=int(input("Enter the Key of the column name needed to be updated :"))
                    break
                except ValueError:
                    print("invalid input ")
                    continue

            if(update<10):
                #Accepting user input Book Number
                BookNo=input("Type the Book No :")

                #Displaying the specific book details
                print("Book details of",BookNo)
                cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE BookNo="'+BookNo+'" ')

                #fetch results from the database
                data= cursor.fetchall()
                for item in data:
                    print("Book Number :",item[0])
                    print("Book Title : ",item[1])
                    print("Author :",item[2])
                    print("Publisher :",item[3])
                    print("Year Published :",item[4])
                    print("Location :",item[5])
                    print("Subject Code :",item[6])
                    print("Price :",item[7])
                    print("ISBN :",item[8])

                #Updating Book Title
                if(update==2):
                    NewTitle=input("Enter new Book Title :")
                    #execute sql query using execute() method.
                    updText="UPDATE book SET Title=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewTitle,BookNo))
                    db.commit() #commit
                    #printing the updated details
                    if(cursor.rowcount==1):
                        print("Title of the book",BookNo,"has been updated to",NewTitle)

                #Updating Book Number
                elif(update==1):
                    NewNo=input("Enter new Book Number :")
                #execute sql query 
                    updText="UPDATE book SET BookNo=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewNo,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Number of the book",BookNo,"has been updated to",NewNo)

                #Updating Subject Code    
                if(update==3):
                    NewSubCode=input("Enter new Subject Code :")
                #execute sql query 
                    updText="UPDATE book SET SubjectCode=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewSubCode,BookNo))
                    db.commit() #commit 
                    if(cursor.rowcount==1):
                        print("Subject Code of the book",BookNo,"has been updated to",NewSubCode)

                #Upadating Author
                if(update==4):
                    NewAuthor=input("Enter new Book Author :")
                #execute sql query
                    updText="UPDATE book SET Author=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewAuthor,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Author of the book",BookNo,"has been updated to",NewAuthor)

                #Updating Publishe
                if(update==5):
                    NewPub=input("Enter new Book Publisher :")
                #execute sql query
                    updText="UPDATE book SET Publisher=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewPub,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Publisher of the book",BookNo,"has been updated to",NewPub)
                        
                if(update==6):
                    NewYear=input("Enter new Published Year :")
                #execute sql query using execute() method.
                    updText="UPDATE book SET YearPublished=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewYear,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Published year of the book",BookNo,"has been updated to",NewYear)
                        
                if(update==7):
                    NewPrice=input("Enter new Book Price :")
                #execute sql query using execute() method.
                    updText="UPDATE book SET Price=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewPrice,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Title of the book",BookNo,"has been updated to",NewPrice)
                        
                if(update==8):
                    NewISBN=input("Enter new Book ISBN :")
                #execute sql query using execute() method.
                    updText="UPDATE book SET ISBN=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewISBN,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("ISBN of the book",BookNo,"has been updated to",NewISBN)
                        
                if(update==9):
                    NewLocation=input("Enter new Book location :")
                #execute sql query using execute() method.
                    updText="UPDATE book SET Location=%s WHERE BookNo=%s"
                    cursor.execute(updText,(NewLocation,BookNo))
                    db.commit() #commit
                    if(cursor.rowcount==1):
                        print("Location of the book",BookNo,"has been updated to",NewLocation)

            else:
                #Updating details in subject table
                SubjectCode=input("Enter the subject code :")
                print("Subject details of",SubjectCode)
                cursor.execute('SELECT SubjectCode,SubjectName FROM subject WHERE SubjectCode="'+SubjectCode+'" ')

                #fetch results from the database
                data= cursor.fetchall()
                for item in data:
                    print("Subject Code :",item[0])
                    print("Subject Name :",item[1])
                #Updating Subject Code
                if(update==10):
                    NewSubject=input("Enter new Subject Code :")
                    #execute sql query using execute() method.
                    updText="UPDATE subject SET SubjectCode=%s WHERE SubjectCode=%s"
                    cursor.execute(updText,(NewSubject,SubjectCode))
                    db.commit() #commit
                    #printing the updated details
                    if(cursor.rowcount==1):
                        print("Subject Code ",SubjectCode,"has been updated to",NewSubject)
                        
                #Updating Subject name
                if(update==11):
                    NewSubName=input("Enter new Subject Name :")
                    #execute sql query using execute() method.
                    updText="UPDATE subject SET SubjectName=%s WHERE SubjectCode=%s"
                    cursor.execute(updText,(NewSubName,SubjectCode))
                    db.commit() #commit
                    #printing the updated details
                    if(cursor.rowcount==1):
                        print("Subject Name of the Subject Code",SubjectCode,"has been updated to",NewSubName)
            return

def delete(cursor,db): #function : delete
            "Delete records from book and subject tables"
            #initialize variables
            delete=0
            BookNo=''
            SubjectCode=''

            while True:
                try:
                    delete=int(input("Enter 1 to delete from Book table or 2 to delete from Subject table :"))
                    break
                except:
                    print("invalid input")

            #Deleting from book table
            if(delete==1):
                BookNo=input("Enter the book number of the book you want to delete :")
                #execute sql query 
                cursor.execute('SELECT BookNo,Title,Author,Publisher,YearPublished,Location,SubjectCode,Price,ISBN FROM book WHERE BookNo="'+BookNo+'" ')
                ##showing selected record before deleting
                data= cursor.fetchall()
                for item in data:
                    print("Book Number :",item[0])
                    print("Book Title : ",item[1])
                    print("Author :",item[2])
                    print("Publisher :",item[3])
                    print("Year Published :",item[4])
                    print("Location :",item[5])
                    print("Subject Code :",item[6])
                    print("Price :",item[7])
                    print("ISBN :",item[8])

                print("Are you sure you want to delete",item[1],"? ") #confirmation
                sure='n'
                while(sure!='y' or sure!='n' ): 
                    sure=input("y/n :")
                    if(sure=='y'):
                        sql = "DELETE FROM book WHERE BookNo = %s"
                        sql1="DELETE FROM chapter WHERE BookNo = %s"
                        cursor.execute(sql1,(BookNo,))
                        cursor.execute(sql, (BookNo,))
                        db.commit() #commit
                        print(BookNo, "book deleted")
                        break
                    elif(sure=='n'):
                        print("No records were deleted")
                        break
                    print("Invalid Input ")
                    
            #Deleting from subject table
            elif(delete==2):
                SubjectCode=input("Enter Subject Code you want to delete :")
                #execute sql query 
                cursor.execute('SELECT SubjectCode,SubjectName FROM subject WHERE SubjectCode="'+SubjectCode+'" ') 
                #showing selected record before deleting
                data= cursor.fetchall()
                for item in data:
                    print("Subject Code :",item[0])
                    print("Subject Name :",item[1])

                print("Are you sure you want to delete",item[1],"? ") #confirmation
                sure='n'
                while(sure!='y' or sure!='n' ): #error handling
                    sure=input("y/n :")
                    if(sure=='y'):
                        sql = "DELETE FROM subject WHERE Subjectcode = %s"
                        cursor.execute(sql, (SubjectCode,))
                        db.commit() #commit
                        print(cursor.rowcount, "record deleted")
                        break
                    elif(sure=='n'):
                        print("No records were deleted")
                        break
                    print("Invalid Input ")


def chapter(cursor): #function : chapter handling
    "write or read book chapters"
    #Initialize variables
    task=0
    new='new'
    while True: #error handling
        try:
            task=int(input("Enter 1 to write chapters, 2 to read chapters :"))
            break
        except:
            print("invalid input")
    while(task==1 and new=='new'):  #write chapters
        BookNo=input('Enter book number :')
        chapter=input("Enter chapter number :")
        print()
        if(BookNo!='' or chapter!=''):
            fo=open(BookNo+'_'+chapter +'.txt','x')
            content=input("Type chapter :")
            fo.write(content)
            fo.close()
        else:
            print("Book number or Chapter number cannot be empty")
        new=input("Type 'new' to write a new chapter. Click enter to exit.")
    if(task==2):  #read chapters
        BookNo=input('Enter book number :')
        chapter=input("Enter chapter number :")
        query="SELECT ChapterTitle FROM chapter WHERE BookNo=%s AND ChapterNo=%s" #getting the chapter title
        cursor.execute(query,(BookNo,chapter))
        data=cursor.fetchall()
        data=str(data).strip("[](),'")  #removing unnecessary brackets and commas
        print(data,'\n')  #printing the chapter title
        fo=open(BookNo+'_'+chapter+'.txt','r')
        print(fo.read())  #printing book contents
        fo.close()
    return 

