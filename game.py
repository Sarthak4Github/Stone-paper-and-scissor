import random

def gamecode(comp,you):
    if comp == you:
        return None

    elif comp == 'snake':
        if you == 'water':
            return False
        else:
            return True

    elif comp == 'water':
        if you == 'gun':
            return False
        else:
            return True

    elif comp == 'gun':
        if you == 'snake':
            return False
        else:
            return True


randno = random.randint(1,3)    

if randno == 1:
    comp = 'snake'
elif randno == 2:
    comp = 'water'  
elif randno == 3:
    comp = 'gun'

print("\n<<<<<<<<<< Snake , Water , Gun Game >>>>>>>>>>>>>>\n")

turn =  int(input("Input best of : "))
i = 1
while(i <= turn):
  i = i + 1
  you = input("Player's turn: Enter input: Snake(s), Water(w) and Gun(g): ")
  res = gamecode(comp,you)
  print(f"computer choose: {comp}")
  print(f"You choose: {you}")
  if res == None:
   print("Its a tie !!")
  elif res == True:
   print("you win!!")
  else:
   print("you lose!!")
   

print("/n Exiting Game......")   
