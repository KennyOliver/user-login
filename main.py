import hashlib

def check_digit(password) -> bool:
  """function: return True if passwords contains a digit otherwise False"""
  digit = False
  for item in password: #check all characters to see if any is digit
    if item.isdigit():
      digit = True
  return digit
#=======================
def get_username() -> str:
  """ function: get username of 8 characters all lower case"""
  name = input("\nEnter username\n--> ")
  while len(name) < 8 :
    name = input("must be 8 characters >")
  username = name
  print("Your chosen username is: ",username)
  return username
#=======================
def get_password() -> str:
  """ function: get password 6 characters and at least on digit"""
  password = input("\nEnter password\n--> ")
  while not( (len(password) >= 8) and (check_digit(password) == True) ) :
    password = input("Must be 8 char and 1 digit\n--> ")
  return password
#=======================
def register():
  user_name = get_username()
  user_password = get_password()
  
  hash_password = hashlib.sha256(user_password.encode("utf-8")).hexdigest()
  
  record = user_name + "," + hash_password + ",\n"
  myfile = open("passwords.txt","a")
  myfile.write(record)
  myfile.close()
  print("Success! 😎")
  
  now_menu = input("Would you like go to the menu now?\n\t[Y] Yes\n\t[N] No\n--> ").upper()
  if now_menu == 'Y':
    menu()
  else:
    print("Re-run the program to access menu.")
#=======================
def login() -> bool:
  """ function: request username & password, check against file records. Return True if found, otherwise false """
  print("Please login with your username and password")
  name = input("\t👤 Username --> ")
  pword = input("\t🔒 Password --> ")
  
  myfile = open("passwords.txt",'r')
  for record in myfile:
    remove_comma = record.split(",")
    rec_name = remove_comma[0]
    rec_password = remove_comma[1]
    #print(remove_comma) #shows that there is a "\n" at the end of every record
    
    hash_pword = hashlib.sha256(pword.encode("utf-8")).hexdigest()
    
    if ((name == rec_name) and (hash_pword == rec_password)) == True:
      print("Success! 😎")
      myfile.close()
      return True
  myfile.close()
  print("⚠️ Invalid username/password!\n⚠️ No entry to the game!")
  return False
#=======================
def menu():
  print("🎮 Welcome! 🎮")
  print("Choose [1] or [2]\n\t[1] Register 📝\n\t[2] Login 👥 ")
  option = input("\t--> ")
  
  while not (option.isdigit() and option in ["1","2"]):
    option = input("Choose [1] or [2]\n--> ")
  
  if option == '1':
    register()
  else:
    if login() == True:
      game()
    else:
      print("👋 Goodbye! 👋")
#=======================
def game():
  print("👾 THIS IS AN AMAZING GAME! 👾")
#=======================
# main program
menu()