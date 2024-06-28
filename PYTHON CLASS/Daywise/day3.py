#------------------------Data types in python------------------------------
int = 1 #integer data type
string = "string" #string data type
float = 1.2 #float data type
complex = 1 + 4j #complex data type 
mapped_data = {"name" : "ram", "address" :"bkt", "age": 19} #dictionary data types
is_boolean = True #boolean data type
#------------Sequenced data--------------
list = [['ram', 'shyam', 'hari'], ["apple", "banana"]] #can be modified
tuple = ("ram", "hari", ) #cannot be modified


#----------------------Length Calculator of an Input-----------------------

# fruitName = input("Ener the name of fruit: ")
# total_length = len(fruitName)
# print(f"Total length of {fruitName} is: {total_length}")

#print fullname
# Fname = input("Enter First Name :")
# Mname = input("Enter Middle name :")
# Lname = input("Enter Last name :")

# fullname = print(f"Your full name is {Fname} {Mname} {Lname}")


#----------------------Add your 10 friend names to list and print all their details-----------------------
name = ['Ram', 'Shyam', 'Gopal', 'Hari', 'Rohit']
address = ['USA', 'KTM', 'BKT', 'UK', 'CANADA']
# print(f"{name[0]} lives in {address[0]}")
# print(f"{name[1]} lives in {address[1]}")
# print(f"{name[2]} lives in {address[2]}")
# print(f"{name[3]} lives in {address[3]}")
# print(f"{name[4]} lives in {address[4]}")

#--------------------Using For Loop-------------------
for i in range(len(name)): 
    print(f"{name[i]} lives in {address[i]}")

#--------------------Using While Loop------------------
# name = ['Ram', 'Shyam', 'Gopal', 'Hari', 'Rohit']
# address = ['USA', 'KTM', 'BKT', 'UK', 'CANADA']

# while True: 
#     friends = input("Enter the name of Friend : ")
#     found = False
    
#     for i in range(len(name)):
#         if friends == name[i]:
#             print(f"{friends} lives in {address[i]}")
#             found = True
#             break
    
#     if not found:
#         print("No such friend's name found in the directory.")
    
#     cont_again = input("Do you want to try searching another friend name? (yes/no): ")
#     if cont_again.lower() == "no":
#         break
#     elif cont_again.lower() != "yes":
#         print("Invalid input. Exiting the program.")
#         break

                   
               
                



