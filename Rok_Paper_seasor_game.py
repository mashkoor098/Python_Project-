# work is progress......
import random as r


def Gresult(comp,user):
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


user= input("What is your choice? 'r' , 'p' , 's'  ")

randomNo = r.randint(1,3)
print("Computer Enterd ")
if randomNo==1:
     comp="r"
elif randomNo==2:
     comp="p"
elif randomNo==3:
     comp="s"

FinalResult= Gresult(comp,user)

print(f"You entered      {user}")
print(f"Computer entered      {comp}")

if FinalResult==None:
     print("Tieeeeeeeeeee")
elif FinalResult:
     print("Winner Winner Chiken Dinner")
else:
     print("You Loos,Better Luck next time")
         
# 1=rock, 2= paper, 3=seasor
