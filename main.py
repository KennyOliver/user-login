def check_digit(password):
 """function returns True if passwords contains a digit otherwise False"""
 digit = False
 for item in password:
   if item.isdigit():
     digit = True
 return digit
#_______________________
def get_username():
 """ function to get username of 8 characters all lower case"""
 name = input("\nEnter username\n--> ")
 while len(name) != 8 :
   name = input("must be 8 characters >")
 username = name.lower()
 print(" you username is ",username)
 return username
#_______________________
def get_password():
 """ function to get password 6 characters and at least on digit"""
 password = input("\nEnter password\n--> ")
 while not( (len(password)==6) and (check_digit(password) == True) ) :
   password = input("must be 6 char and one digit> ")
 return password
#_______________________
def register():
 user_name = get_username()
 user_password = get_password()
 record = user_name + "," + user_password + ","
 myfile = open("passwords.txt","a")
 myfile.write(record)
 myfile.close()
 print("Welcome - successful registration")
 
#main program
#register()

#=======================
def login():
  """ function: request username & password, check against file records. Return True if found, otherwise false """
  print("Please login with your username and password")
  name = input("Username\n--> ")
  pword = input("Password\n--> ")
  
  myfile = open("passwords.txt",'r')
  for record in myfile:
    remove_comma = record.split(",")
    rec_name = remove_comma[0]
    rec_password = remove_comma[1]
    #print(remove_comma) #shows that there is a "\n" at the end of every record
    
    if ((rec_name == name) and (rec_password == pword)) == True:
    #if rec_password == pword:
      print("Valid username and password entered!")
      myfile.close()
      return True
  myfile.close()
  print("Invalid username/password!\nNo entry to the game!")
  return False
#=======================
def menu():
  print("Welcome!")
  print("[1] Register\n[2] Login")
  option = input("Choose [1] or [2]\n--> ")
  
  while not (option.isdigit() and option in ["1","2"]):
    option = input("Choose [1] or [2]\n--> ")
  
  if option == '1':
    register()
  elif option == '2':
    if login() == True:
      game()
    else:
      print("\nGoodbye!")
#=======================
def game():
  print("THIS IS AN AMAZING GAME!")
#=======================
# main program
menu()