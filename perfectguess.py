import random
number = random.randint(1,20) # the limit of guessing is 20
guess = int(input("enter the number"))
attemts = 1
# the game is about guessing a number
while(True):
    if(guess > number):
      guess = int(input("enter another number.this one is too high :"))
      attemts+=1
    elif(guess < number):
      guess = int(input("enter another number.this one is too low: "))
      attemts+=1
    elif(number > 20):
       print("out of limit")  
    else:
       print(f"you won in {attemts} attempts")
       break
points1 = attemts
print(points1)
# level 2

import random
number = random.randint(1,40) # the limit of guessing is 20
guess = int(input("enter the number"))
attemts = 1
# the game is about guessing a number
while(True):
    if(guess > number):
      guess = int(input("enter another number.this one is too high :"))
      attemts+=1
    elif(guess < number):
      guess = int(input("enter another number.this one is too low: "))
      attemts+=1
    elif(number > 40):
       print("out of limit")  
    else:
       print(f"you won in {attemts} attempts")
       break
points2 = attemts
print(points2)

# you have crossed level 2
import random
number = random.randint(1,100) # the limit of guessing is 20
guess = int(input("enter the number"))
attemts = 1 
# the game is about guessing a number
while(True):
    if(guess > number):
      guess = int(input("enter another number.this one is too high :"))
      attemts+=1
    elif(guess < number):
      guess = int(input("enter another number.this one is too low: "))
      attemts+=1
    elif(number > 100):
       print("out of limit")  
    else:
       print("you won this match")
       break
points3 = attemts
print(points3)
# for calling the total score

def total():
   total = points1 + points2 + points3
   print(total)
# 30 is the margin

   if(total > 30):
     print("you are third")
   elif(total == 30):
      print("you are second")
   else :
      print("you are first")
total()

# level 3 finished you won with the score you scored 