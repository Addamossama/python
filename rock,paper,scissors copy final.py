#definitions
import random
def say_hello(thename):
 print('hello'.capitalize(),thename,"!",'welcome to Rock-Paper-Scissors!'.capitalize())
choices =["rock",'paper',"scissors"]
username=input("enter username: ")
say_hello(f'{username}')
wincount=0
losecount=0
tiecount=0

#
userchoice=input("enter your choice: ")
computer=random.choice(choices)
#print("username:",userchoice,'\tcomputer:'.expandtabs(20),computer)
result1=('it\'s a tie!'.capitalize())
result2=("you win!".capitalize())
result3=("you lose!".capitalize())
answer=("this is not a valid answer!!".upper())
def myfunc():
 print(f"\t{username} chose:".expandtabs(63),userchoice,'\tcomputer chose:'.expandtabs(11),computer)#the f sting is only usef when typing variable with string meaning you can type the variable and use + and type the string
def myfunc1():
 print("\t".expandtabs(80),result1)
 global tiecount
 tiecount+=1
def myfunc2():
 print("\t".expandtabs(80),result2)
 global wincount
 wincount+=1
def myfunc3():
 print("\t".expandtabs(80),result3,)
 global losecount
 losecount+=1
 
#gameplay
if computer==userchoice:
  myfunc(),myfunc1()
elif computer=="rock":
 if userchoice=='scissors':
  myfunc(),myfunc3()
 if userchoice=='paper':
  myfunc(),myfunc2()
elif computer=="paper":
 if userchoice=='scissors':
  myfunc(),myfunc2()
 if userchoice=='rock':
  myfunc(),myfunc3()
elif computer=="scissors":
 if userchoice=='rock':
  myfunc(),myfunc2()
 if userchoice=='paper':
  myfunc(),myfunc3()
if userchoice not in choices:
 print('\t'.expandtabs(90),answer)


#replay(loop)
replay=input('do you want to play again?(yes or no):')
if replay=='no':
 count=input('do you want to see your count?(yes or no)')
 if count=='yes':
     print("your win count is "+str(wincount)+" ,your lose count is "+str(losecount)+" ,your tie count is "+str(tiecount))
     print(f'Thanks for playing! Goodbye {username} !.');pass;p=input("press enter to exit")#this input is for keeping python open
 if count=='no':
     print(f'Thanks for playing! Goodbye {username} !.');pass;p=input("press enter to exit")#this input is for keeping python open
 while count!='yes' and count!= 'no':
     print('\t'.expandtabs(90),answer)
     count=input('do you want to see your count?(yes or no)')#there is problem here that if answer is not yes or no then you type yes or no it closes you can fix it by using while instead of if
while replay=='yes':
  userchoice=input("enter your choice: ")
  computer=random.choice(choices)
  if computer==userchoice:
    myfunc(),myfunc1()
  elif computer=="rock":
   if userchoice=='scissors':
    myfunc(),myfunc3()
   if userchoice=='paper':
    myfunc(),myfunc2()
  elif computer=="paper":
   if userchoice=='scissors':
    myfunc(),myfunc2()
   if userchoice=='rock':
    myfunc(),myfunc3()
  elif computer=="scissors":
   if userchoice=='rock':
    myfunc(),myfunc2()
   if userchoice=='paper':
    myfunc(),myfunc3()
  if userchoice not in choices:
   print('\t'.expandtabs(90),answer)
  replay=input('do you want to play again?(yes or no):')
  if replay=='no':
   count=input('do you want to see your count?(yes or no)')
   if count=='yes':
     print("your win count is "+str(wincount)+" ,your lose count is "+str(losecount)+" ,your tie count is "+str(tiecount))
     print(f'Thanks for playing! Goodbye {username} !.');pass;p=input("press enter to exit")#this input is for keeping python open
   if count=='no':
     print(f'Thanks for playing! Goodbye {username} !.');pass;p=input("press enter to exit")#this input is for keeping python open
   while count!='yes' and count!= 'no':
     print('\t'.expandtabs(90),answer)
     count=input('do you want to see your count?(yes or no)')
  while replay!='yes' and replay!='no':
    print('\t'.expandtabs(90),answer)
    replay=input('do you want to play again?(yes or no):')
while replay!='yes' and replay!='no':
    print('\t'.expandtabs(90),answer)
    replay=input('do you want to play again?(yes or no):')