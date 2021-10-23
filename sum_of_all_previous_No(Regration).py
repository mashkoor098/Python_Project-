def sumAll(inp):
    
     if inp == 1:
          return 1
     else:
          ans=inp+sumAll(inp-1)
          return ans
     

inp=int(input("Enter a Number that you want to calculate all previous addition_________  "))
print(f"Sum of all previous Numbers from_{inp}_ is ___=",sumAll(inp))

# this program calculate all previous number from the given number.
# for Ex: user Entered : 3
# then it calculate : 1+2+3=6
# It's a type regration
