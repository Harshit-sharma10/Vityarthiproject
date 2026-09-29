

#VITYARTHI PROJECT

#RANDOM MOBILE NUMBER ASSIGNER


import random

  
users={}

# 1. Generate


def genmob():
    while True:
        firstdig=random.choice("6789")
        remainingdig=""
        for i in range(9):
            dig=str(random.randint(0,9))
            remainingdig=remainingdig+dig

        mob=firstdig+remainingdig

        if mob not in users.values():
            return mob


#  2.Assign



def assignnum():
    print("\nAssigning a mobile number to you")

    name=input("Enter your name= ").strip()
    if(name==""):
        print("Name cannot be empty")
        return
    if(name in users):
        print("Name is already registered")

    try:

        age=int(input("Enter the age= "))


        if(age<=0 and age>120):
            print("\nEnter valid age")
            return
    except ValueError:
        print("Age must be a number")
        return

    mob=genmob()

    users[name]={"age":age,"mob":mob}

    print("\nRegistration sucessfully")
    print("Name=",name)
    print("Age=",age)
    print("Assigned Mobile Number=",mob)


#3.Search 



def searchuser():
    print("\n----------- Searching User-----------")

    name=input("Enter the name= ")

    if(name in users):
        print("Name is=",name)
        print("Age is=",users[name]["age"])
        print("Mobile number is",users[name]["mob"])


    else:
        print("User not found")



# 4.Display 



def  displayusers():
    print("All registered users are following: ")

    if(len(users)==0):
        print("No user registered in database")
        return

    count=1

    for name,details in users.items():
        print("\nUsers",count)
        print("Name",name)
        print("Age",details["age"])
        print("Mobile number",details["mob"])

        count+=1


# 5.Update 


def updateage():
    print("\n----Updateding your  Age")

    name=input("Enter the name=").strip()
    if(name not in users):
        print("User not found")
        return
    try:
        age=int(input("Enter the age="))
        if(age<0 and age>120):
            print("Enter a valid age")
            return
    except ValueError:
        print("Age must be valid")
        return
    users["age"]=age


    print("Age updated sucessfully")



#6.Delete



def deluser():
    print("\n-------Updating user---------")


    name=input("Enter the name=")

    if name in users:
        del users[name]
        print("User deleted sucessfully")

    else:
        print("User not found")



#7.Count 
def countusers():
    print("\n Total numberof users are= ",len(users))


#
#7.Save
#
def saveusers():
    with open("Users.txt","a") as file:
        for name,details in users.items():
            age=details["age"]
            mob=details["mob"]

            file.write(name+"|"+str(age)+"|"+mob+"\n")

#8.load


def loadusers():
    try:
        with open("Users.txt","r") as file:
            for line in file:
                line=line.strip()

                if(line==""):
                    continue
                data=line.split("|")

                if(len(data)==3):
                    name=data[0]
                    age=int(data[1])
                    mob=data[2]

                    users[name]={"age":age ,"mob": mob}
    except FileNotFoundError:
        print("No previous data found")
    except ValueError:
        print("Invalid data in file")
    



#9.MainMenu

while True:
    print("RANDOM MOBILE NUMBER ASSIGNER==============")

    print("Choose your request from given list")
    print(" Assigning random mobile number code: 1")
    print("Search user code: 2")
    print("Display all user code: 3")
    print("Update age code: 4")
    print("Delete user code: 5")
    print("Count user code: 6")
    print("Exit code: 7")



    request=int(input("Enter your request code="))

    loadusers()
    if(request==1):
        loadusers()
        assignnum()
        saveusers()
        
    elif(request==2):
        loadusers()
        searchuser()

    elif(request==3):
        loadusers()
        displayusers()
    
    elif(request==4):
        loadusers()
        updateage()
        saveusers()
    
    elif(request==5):
        loadusers()
        deluser()
        saveusers()

    elif(request==6):
        loadusers()
        countusers()
        
    elif(request==7):
        break
    else:
            print("Provide a valid input code\nPlese try again")

    proceed=input("Want to proceed further? (yes/no): ")
    if(proceed.lower()!="yes"):
        break
print("REQUEST COMPLETED")