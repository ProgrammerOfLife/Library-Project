class NewUser(object):
    def __init__(self, Name):
        Number_of_Users = 0        
        Number_of_Users =+1
        self.Name = Name
        self.Serial_Number = Number_of_Users
        self.Library_Id = "ZionLib" + str(Number_of_Users)
    def Details(self):
        return "Welcome " + self.Name  + " This is your serial number : %d" %(self.Serial_Number) + " and your library Id is: " + self.Library_Id 

        

Invalid_input = "Your Input is not valid"
Next = "press enter to continue"
Question = "Are you a Library user or a Librarian: "
print (" Welcome to Zion Library, we are so hapi to have you here")
input(Next)
print ("My name is Lemh your Library guide. I am here to make things easy for you, i know everything about this Library")
input(Next)
print (Question)
Res1 = input("*Pls answer with either 'User' or 'Librarian'*: ").upper()
if Res1 == "USER":
    print ("Great welcome one again to Zoin Library!!!")
    input(Next)
    print ("Are you a registered Zion Library User?")
    Res2 = input("*Please answer with either 'Yes' or 'No'*: ").upper()
    if Res2 == "YES":
        print ("Welcome Back Citizen of Zion")
    elif Res2 == "NO":
        print ("Am sorry you cant access this Library except u are a registered member.")
        input(Next)
        print ("Would you like to register?")
        Res3 = input("*Please answer with either 'Yes' or 'No'*: ").upper()
        if Res3 == "YES":
            print ("Lets start the registration")
            input(Next)
            User_input = input("Please whats is your name? ")
            Create = NewUser(User_input)
            print (Create.Details())
        elif Res3 == "NO":
            print ("Am so sorry you can`t continue because you are not a memeber and you are not willing to be one")
        else:
            print (Invalid_input)
    else:
       print (Invalid_input)
