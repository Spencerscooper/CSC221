#Challenge 
from random import randint
num1 = randint(1,10)
num2 = randint(1,10)
print(2*("What is", num1,"times", num2))
answer = int(input("Type in your answer \n"))
if num1 * num2 == answer:
    print("yes")
else:
    print("Wrong your answer should have been", num1*num2)



#Challenge5
