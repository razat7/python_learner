## Random Number Generator
import random
random_number = random.randint(1,20)
user_input = int(input("Enter your Number Between 1-20 : "))
if user_input == random_number:
    print(f"Congratulations The Number is {random_number}")
else:
    print("Well Tried, You can try one more time :")
    user_input = int(input("Enter the number Again : "))
    print(f"Sorry, Actual Number is {random_number}")
   
#Random String Generator
# person_name = ['Ram', 'Hari', 'Sita']
# winner = random.choice(person_name)
# print(winner)

# password = random.randint(-20, -10)
# print(f"Random Number is {password}")

# numbers = random.randint(10, 20)
# print(f"Random Number is -{numbers}")

# git checkout master