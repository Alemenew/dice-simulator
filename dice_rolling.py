import random

print ("this is the dice simulator")
x = "y"
while x == "y":
    number = random.randint(1,6)
    if number == 1:
        print ('------------')
        print ('|          |')
        print ('|    O     |')
        print ('|          |')
        print ('------------')
    elif number == 2:
        print ('------------')
        print ('|          |')
        print ('| O      O |')
        print ('|          |')
        print ('------------')
    elif number == 3:
        print ('-----------')
        print ('|    O    |')
        print ('|    O    |')
        print ('|    O    |')
        print ('-----------')

    elif number == 4:
        print ('------------')
        print ('| O      O |')
        print ('|          |')
        print ('| O      O |')
        print ('------------')
    elif number ==5:
        print ('------------')
        print ('| O      O |')
        print ('|     O    |')
        print ('| O      O |')
        print ('------------')

    elif number ==6:
        print ('--------------')
        print ('| O       O  |')
        print ('| O       O  |')
        print ('| O       O  |')
        print ('--------------')

    x = input ("enter y to continue or enter any key to exit")
