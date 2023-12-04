from random import randint
#Challenge1

number_one = randint(1,10)
number_two = randint(1,10)
print(f"What is {number_one} times {number_two}")
answer = number_one * number_two
print(answer)

#Challenge2
number_one = randint(1,10)
number_two = randint(1,10)
print(f"What is {number_one} plus {number_two}")

result = number_one + number_two
print(result)


#Challenges3

number_one = randint(1,10)
number_two = randint(1,10)
answer = int(input(f"What is {number_one} times {number_two} ?\n"))
if number_one * number_two == answer:
    print(f"Your answer {answer} is correct!!")
else:
    print(f"Wrong")

#Challenge4
number_one = randint (1,10)
print(str(number_one) * 5)


