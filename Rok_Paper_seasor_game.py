import random as r

# Input validation function
def get_user_input():
    while True:
        user_input = input("What is your choice? 'r' , 'p' , 's'  ").lower()
        if user_input in ['r', 'p', 's']:
            return user_input
        else:
            print("Invalid input! Please enter 'r', 'p', or 's'.")

def Gresult(comp, user):
     if comp=="r":
          if user == comp:
               return None
          elif user == "p":
               return 1
          elif user == "s":
               return 0

     elif comp=="p":
          if user == "r":
               return 0
          elif user == "s":
               return 1

     elif comp=="s":
          if user == "r":
               return 1
          elif user == "p":
               return 0

# Get user input with validation
user = get_user_input()

randomNo = r.randint(1, 3)
print("Computer Entered ")
if randomNo==1:
     comp="r"
elif randomNo==2:
     comp="p"
elif randomNo==3:
     comp="s"

FinalResult = Gresult(comp, user)

print(f"You entered      {user}")
print(f"Computer entered      {comp}")

if FinalResult == None:
     print("Tieeeeeeeeeee")
elif FinalResult:
     print("Winner Winner Chicken Dinner")
else:
     print("You Lose, Better Luck Next Time!")
