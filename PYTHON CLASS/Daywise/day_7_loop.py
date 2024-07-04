##-----------------------------LOOPS-------------------------
#Do, While Loops

# number = 10  
# for i in range(number):
#     result = i * 9
#     print(f"9 * {i} = {result}")

#nested loop
# numb1 = int(input("Enter Starting Number : "))
# numb2 = int(input("Enter End Number : "))
# for i in range(numb1, numb2):
#     for j in range(1,10):
#         print(f"{i}*{j} = {i*j}")
#     print("------------------")

#using for loops
# fruits = []
# print("Fruits Chart")

# num_fruits = int(input("Enter the number of fruits : "))
# for i in range (1, num_fruits+1):
#     name_fruit = input(f"Enter the name of fruits :  {i} ")
#     fruits.append(name_fruit)
# print (fruits)

#while loops
# atm_pin = '1456'
# user_pin = ''
# attempt = 0
# while atm_pin != user_pin:
#    if attempt>0:
#     print("Invalid Pin")
#    user_pin = input("Enter Atm Pin")
#    attempt = attempt + 1
# print("Access Granted")


# scores = [45,45,44,55,67]
# for score in scores:
#   if score>50:
#     print(f"Score is {score} : Pass")
# else:
#     print(f"Score is {score} : Fail")

##Pin verifying using while loop

# pin = '1234'
# userpin = ''
# attempt= 0
# while attempt < 4:
#     userpin = input("Enter Your Pin : ")
#     if userpin == pin:
#         print("The entered pin is correct")
#         break
#     else:
#         attempt +=1
#         print("*Pin is incorrect")
# else:
#     print("Too many attempts, You are blocked.")
