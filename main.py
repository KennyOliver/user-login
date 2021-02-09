import hashlib

def check_digit(password) -> bool:
  """ if password contains 1+ digit, return True, else False """
  
  digit = False
  for char in password: #see if any character is digit
    if char.isdigit():
      digit = True
  return digit
#=======================
def get_username() -> str:
  """ get username of 8+ char """
  
  username = input("\nEnter username\n--> ")
  while len(username) < 8:
    username = input("Must be at least 8 characters --> ")
  print(f"Your chosen username is: {username}".format(username))
  return username
#=======================
def get_password() -> str:
  """ get password 8+ char and at 1+ digit"""
  
  password = input("\nEnter password\n--> ")
  while not((len(password) >= 8) and (check_digit(password) is True)):
    password = input("Must be 8 char and 1 digit\n--> ")
  return password
#=======================
def register():
  """ registration """
  
  username = get_username()
  userPass = get_password()
  
  hashPass = hashlib.sha256(userPass.encode("utf-8")).hexdigest()
  
  record = username + "," + hashPass + "," + "\n"
  myfile = open("passwords.txt",'a')
  myfile.write(record)
  myfile.close()
  print("Success! 😎\n")
  
  now_menu = input("Would you like go to the menu now?\n\t[Y] Yes\n\t[N] No\n--> ").upper()
  if now_menu == 'Y':
    menu()
  else:
    print("Re-run the program to access the menu.")
#=======================
def login() -> bool:
  """ request username & password, check against file records. If found, return True, else False """
  print("")
  print("Please login with your username and password")
  
  username = input("\t👤 Username --> ")
  pword = input("\t🔒 Password --> ")
  
  myfile = open("passwords.txt",'r')
  for record in myfile:
    remove_comma = record.split(",")
    rec_username = remove_comma[0]
    rec_password = remove_comma[1]
    #print(remove_comma) #shows that there is a "\n" at the end of every record
    
    hash_pword = hashlib.sha256(pword.encode("utf-8")).hexdigest()
    
    if ((username == rec_username) and (hash_pword == rec_password)) is True:
      print("Success! 😎\n")
      myfile.close()
      return True
  
  myfile.close()
  print("⚠️ Invalid username/password!\n⚠️ No entry to the game!")
  return False
#=======================
def menu():
  """ main menu """
  
  print("\n")
  print("-" * 15)
  print("🎮 Welcome! 🎮")
  print("-" * 15)
  print("\n")
  
  print("Choose action:\n\t[1] Register 📝\n\t[2] Login 👥 ")
  option = input("\t--> ")
  
  while not (option.isdigit() and option in ["1","2"]):
    option = input("Choose [1] or [2]\n--> ")
  
  if option == '1':
    register()
  else:
    if login() is True:
      game()
    else:
      print("👋 Goodbye! 👋")
#=======================
def game():
  print("")
  print("👾 THIS IS AN AMAZING GAME! 👾")
#=======================
# main program
menu()