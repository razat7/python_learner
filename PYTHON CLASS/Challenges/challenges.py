###------------------- Day 1  Challenges------------------------------
# print(" Hello world ! This is my first program")
# print("My name is Razat Khadka")
# print("I am from Suryavinayak, Bhaktapur")
# print("Currently, I am voluntering as UN Peacekeeper in UNMISS")
# print(" I am 28 years old")
# print("I am from Nepal")
# print("I am learning python")
# print("Our class will end in shrawan 15")
# print("We are going to learn various types of project based exercise in python")
# print("Python can be used in various ")

###------------------- Day 2  Challenges------------------------------
# sunday = 200
# monday = 300
# tuesday = 300
# wednesday = 400
# thursday = 500
# friday = 1000
# saturday = 2000

# total_expenses = sunday+monday+tuesday+wednesday+thursday+friday+saturday
# average_exepenses = total_expenses/ 7
# print (f"My Total Expenses in a Week is: \t {total_expenses}")
# print (f"My Weekly Average Expenses is : \t {average_exepenses}")

###------------------- Day 3  Challenges------------------------------

# name = ['Ram', 'Shyam', 'Gopal', 'Hari', 'Rohit']
# address = ['USA', 'KTM', 'BKT', 'UK', 'CANADA']

# #Using for loop
# # for i in range(len(name)): 
# #     print(f"{name[i]} lives in {address[i]}")

# print(f"{name[0]} lives in {address[0]}")
# print(f"{name[1]} lives in {address[1]}")
# print(f"{name[2]} lives in {address[2]}")
# print(f"{name[3]} lives in {address[3]}")
# print(f"{name[4]} lives in {address[4]}")

###------------------- Day 4 Challenges------------------------------

# expenses = {
#     'January': 1100,
#     'February': 1000,
#     'March': 1500,
#     'April': 1200,
#     'May': 1000,
#     'June': 900,
#     'July': 800,
#     'August': 1000,
#     'October': 600,
#     'September': 400,
#     'November': 800,
#     'December': 200,
# }
# print("---Billing Amount of Year 2080---")
# print("Month\tAmount(inRs)")

# total_amount = sum(expenses.values())
# discounted_rate = 0.05
# discount_amount = total_amount * discounted_rate
# pay_amount = total_amount-discount_amount
# average_amt = sum(expenses.values()) / len(expenses.values())
# for key, value in expenses.items():
#     print(f"{key} : Rs.{value}")

# print(f"Average Amount is {average_amt}")
# print(f"Total Amount : {total_amount}")

# print (f"The total amout to be paid after discount is : Rs.{pay_amount}")


###------------------- Day 5 Challenges------------------------------
# ------------1. Create a programme that Converts NRS to USD, Japanese & Euro------------
# ------------ Enter amount in NRS : # USD , Euro, Japanese Yen :------------

# print("currency converter".upper())
# print("all ex rate are as of 2024-Jun 21".upper())
# nepali_currency = input("Enter Nepali Currency (Amount in Rs : )")
# us_exchange_rate = 0.007474 
# euro_exchange_rate = 0.0070 
# japanese_exc_rate = 0.84
# usconverter = int(nepali_currency)*us_exchange_rate
# euroconverter =  int(nepali_currency)*euro_exchange_rate
# japaneseconverter =  int(nepali_currency)*japanese_exc_rate
# askUser = int(input("Choose the currency type you want to convert : \n1-Us\n2-Euro\n3-Japanese Yen\nChoose : "))
# if askUser == 1:
#     print(f"US exchange rate as of today is $ {usconverter}".upper())
# elif askUser ==2:
#     print(f"euro exchange rate as of today is € {euroconverter}".capitalize())
# elif askUser ==3:
#     print(f"Japanese yen exchange rate as of today is  ¥ {japaneseconverter}")
# else:
#     print("Try Again in few minutes, System is busy".upper())

# ------------2. Create a programme that calculates Temperature------------

# conversion = int(input("Enter the conversion you want: \n 1 : °Farenheit to °Celsius\n 2 : °Celsius to °Farenheit\n 3 : °Farenheit to Kelvin \n 4 :  Kelvin to °Farenheit \n 5 :  °Celsius to Kelvin  \n 6 :  Kelvin to °Celsius \n 7 :  Convert All \n \nEnter Number :"))
# if conversion == 1:
#     farenheit = int(input("Enter the Temperature in °Farenheit : "))
#     calc_1 = (farenheit-32)*5/9
#     print(f"Temperature is : {round(calc_1, 2)}°Celsius") #round(int, 2) & (int: .2f) are used here to trim the data after point
# elif conversion == 2:
#     celsius =  int(input("Enter the Temperature in °Celsius : "))
#     calc_2 = (celsius*9/5)+32
#     print(f"Temperature is : {round(calc_2, 2)}°Farenheit")
# elif conversion == 3:
#     farenheit_1 =  int(input("Enter the Temperature in °Farenheit : "))
#     calc_3 = (farenheit_1*32)*5/9+273.15
#     print(f"Temperature is : {round(calc_3, 2)} Kelvin")
# elif conversion == 4:
#     kelvin =  int(input("Enter the Temperature in Kelvin : "))
#     calc_4 = (kelvin-273.15)*9/5+32
#     print(f"Temperature is : {round(calc_4, 2)}°Farenheit")
# elif conversion == 5:
#     celsius_1 =  int(input("Enter the Temperature in °Celsius : "))
#     calc_5 = (celsius_1)+273.15
#     print(f"Temperature is : {round(calc_5, 2)} Kelvin")
# elif conversion == 6:
#     kelvin_1 =  int(input("Enter the Temperature in Kelvin : "))
#     calc_6 = (kelvin_1)-273.15
#     print(f"Temperature is : {round(calc_6, 2)} °Celsius : ")
# elif conversion == 7:
#     temperature = int(input("Enter Any Random Digit : "))
#     print(f"the coversion of {temperature}°F to °C is : {temperature-32*5/9: .2f} °C")
#     print(f"the coversion of {temperature}°C to °F is : {temperature*9/5+32: .2f} °F")
#     print(f"the coversion of {temperature}°F to K is : {(temperature-32)*5/9+273.15: .2f} K")
#     print(f"the coversion of {temperature} K to °F is : {(temperature-273.15)*9/5+32: .2f} °F")
#     print(f"the coversion of {temperature}°C to K is : {temperature+273.15: .2f} K")
#     print(f"the coversion of {temperature} K to °C is : {temperature-273.15: .2f} °C")# else:
#     print("System is Busy, Please Try Again in Few Minutes".upper())


# ------------3. Create a programme that calculates BMI------------
# print("---------------BMI CALCULATOR---------------\n")
# print("Result is based on the data provide by users\n".upper())

# # height = float(input("Enter Your Height (in cm) : "))
# actual_height = float(input("Enter Your Height (in inches) : "))
# weight = float(input("Enter Your Weight  (in kgs) : "))
# age = int(input("Enter Your Age : "))
# bmi = weight/ (actual_height * actual_height)
# print(f"Your BMI : {round(bmi, 2)}\n")
# if bmi >= 25 and bmi <=30 and age < 50:
#     print ("You are overweight, You need to do some workout. ")
# elif bmi >=25 and bmi <=27 and age >= 50:
#     print ("According to your age, you are excused but you should start doing light exercise.")
# elif bmi >= 18.5 and bmi <=24.9:
#     print("Enjoy, You are having a healthy lifestyle.")
# elif bmi < 18.5 :
#     print("You need review your workout schedule and diet plan, or You can go for a doctoe.")
# elif bmi > 30 :
#     print("You are hugely obese person, Maintain your BMI to stay fit & healthy")
# else:
#     print("There's something wrong, Please check Again")

# -----4. Develop a basic calculator that performs addition, subtraction, multiplication, and division based on user input-----
# print("Prompt Calcualator".upper())
# input1 = int(input("Enter First Number : "))
# operator = input("Enter Operator : ")
# input2 = int(input("Enter Second Number : "))
# if operator == '+':
#     sum = input1+input2
#     print(f"Sum of {input1} and {input2} is : {sum}")
# elif operator == '-':
#     sub = input1-input2
#     print(f"Subtraction of {input1} and {input2} is : {sub}")
# elif operator == '/':
#     div = input1 / input2
#     print(f"Division of {input1} and {input2} is : {div}")
# elif operator == '%':
#     mod = input1 % input2
#     print(f"Modulus of {input1} and {input2} is : {mod}")
# elif operator == '**': #exponentiation(power calculation)
#     square = input1 ** input2
#     print(f"Square of {input1} and {input2} is : {square}")
# elif operator == '//': #results quotient
#     intDiv = input1//input2
#     print(f"Int Division of {input1} and {input2} is : {intDiv}")
# else:
#     print("There's something wrong, Please Try again....")

# -----5. Write a script that calculates the tip amount based on the bill total and desired tip percentage entered by the user-----
# def bill(billAmt, tipsPercent):
#     tipsAmt = billAmt *(tipsPercent/100)
#     return tipsAmt

# billAmt = int(input("Enter the total bill amount : "))
# tipsPercent = int(input("Enter the tips percentage : "))

# tipsAmt = bill(billAmt, tipsPercent)
# print(f"Total tips amount will be : Rs.{tipsAmt}")

# -----6.  Create a simple password generator-----
# import random
# print("Password Genertor")
# alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
# number = "1,2,3,4,5,6,7,8,9,0"
# characters = "!,@,#,$,%,^,&,*"
# pw_print = alphabet + number + characters
# combined_pw = pw_print.split(",")
# random1 = random.choice(combined_pw)
# random2 = random.choice(combined_pw)
# random3 = random.choice(combined_pw)
# random4 = random.choice(combined_pw)
# random5 = random.choice(combined_pw)
# random6 = random.choice(combined_pw)
# random7 = random.choice(combined_pw)
# random8 = random.choice(combined_pw)
# password = random1+random2+random3+random4+random5+random6+random7+random8
# print(f"Generated Password is : {password}")

# -----7.  Create a Simple Name Generator-----

# import random
# name = input("Enter name : ")
# symbol = '@'
# number = "1,2,3,4,5,6,7,8,9,0"
# randomNum = number.split(",")
# rand_1 = random.choice(randomNum)
# rand_2 = random.choice(randomNum)
# rand_3 = random.choice(randomNum)
# username = symbol+name+rand_1+rand_2+rand_3
# print(username)

#7.1-----------Option2-----------
# import random
# name = input("Enter your name :") #Take Name From User
# char = "@"
# parts = name.split() #Splitted full name 
# firstpart = parts[0].lower() #Convert uppercase letter to small 
# random_numbers = random.randint(100,9999) #Choosen random number

# print(f"Username is :{char}{firstpart}{random_numbers}")

#-----8.  Create a Simple QR Email Generator-----
# import qrcode
# email_address = 'razat.khadka729@gmail.com'
# subject = "My First Email Using Python"
# body = " Hello, this is my first email using Python."
# mailto = f"mailto:{email_address}?subject={subject}&body={body}"
# img = qrcode.make(mailto)
# type(img)
# img.save("email.png")

#--------------------Date Converter------------------------
#datae conversion module
# import datetime
# import datetime_nepali

# year = int(input("Enter Nepali Year : "))
# month = int(input("Enter Nepali Month : "))
# day = int(input("Enter Nepali Day : "))
# date = datetime_nepali.date(year, month, day).to_datetime_date()
# print(f"The Converesion of Nepali Date is : {date}")

#Write a Python program that prompts the user to enter a number corresponding to a month 
# (1 for January, 2 for February, ..., 12 for December). The program should then display the name of the month based on the number entered.

# months = int(input("Enter the number of Months : "))

# if months ==1:
#     print(f"The Month {months} is January")
# elif months == 2:
#   print(f"The Month {months} is February")
# elif months == 3:
#      print(f"The Month {months} is March")
# elif months ==4:
#     print(f"The Month {months} is April")
# elif months == 5:
#     print(f"The Month {months} is May")
# elif months ==6:
#     print(f"The Month {months} is June")
# elif months ==7:
#     print(f"The Month {months} is July")
# elif months ==8:
#     print(f"The Month {months} is August")
# elif months ==9:
#    print(f"The Month {months} is October")
# elif months ==10:
#     print(f"The Month {months} is September")
# elif months == 11:
#     print(f"The Month {months} is November")
# elif months ==12:
#     print(f"The Month {months} is December")
# else:
#     print("There's something wrong, Please try again in a while.")

#Option 2 (Using Dictionary Data Type)
# month = {'1':'january', '2':'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june', '7': 'july', '8': 'august', '9': 'october', '10': 'september', '11': 'november', '12': 'december'}
# user11 = str(input("Enter the number of months : "))
# if user11 in month:
#     print(f"The month is {(month[user11]).upper()}")
# else:
#     print("Please try again in few minutes")

#-------------Display your name 1000 times using loop in python.------------

# username = input("Enter your name :")
# for i in range (1, 101):
#     print(f"{i}. {username}")

#------------using while loop-----------------------------
# number = int(input("Enter any number you want to multiply : "))
# for i in range (100): #i is variable that holds the range of a number there in range from 1 to 100
#     print(f"{number}*{i}={number * i}")

# number = 0
# while number < 10:
#     print(f"number id {number}")
#     number += 1
# print ("count ends")
        
# password = "12345"
# attempt = 0
# max_attempt = 3

# while attempt < max_attempt: #applying while condition 
#     userpasss = input("Enter the password :") #asking user to input the password
#     if userpasss == password: #comparing user input password with right password
#         print("Right password")
#         break #While true case ends here

#     else:
#         attempt += 1 
#         if attempt == max_attempt:
#             print("Maximum Limit Reached")
#         else:
#             print("Password Wrong")

# num = int(input("Enter the number : "))

# if num <= 0:
#     print("Please enter positive number")
# else:
#     countdown = num
#     while countdown >= 0:
#         countdown -= 1
#         print(countdown)


# import random #imorting module
# def passwordGenerator(length): #creating a function name passwordGenrator

#     alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
#     number = "1,2,3,4,5,6,7,8,9,0"
#     characters = "!,@,#,$,%,^,&,*"

#     pw_print = alphabet + number + characters

#     combined_pw = pw_print.split(",") #Splitting commas from the joined password characteres

#     userpassword = ''.join(random.choice(combined_pw) for i in range (length))  
#     #The '' (empty string) before .join is used as the separator, meaning that the characters are joined without any additional characters between them.
    
#     return userpassword

# length = int(input("Enter the length of a password : "))
# if length <= 0:
#     print("Password Length cannot be null or negative number")
# userpassword = passwordGenerator(length)
# print(userpassword)



# print("=================")

# new_pass = passwordGenerator(5) #callinfg the function to declare value 
# print(new_pass)


# Example usage:
# def square_Number(number):
#     number = number**2
#     return(number)

# number = square_Number(4)
# print(number)

# def roundNumber(n):
#     number = round(n)
#     return number

# num1 = roundNumber(3.11)
# print(num1)

name = [
    # name , department
    ("santosh", "IT"),
    ("manish", "IT"),
    ("sujan", "MBA"),
    ("hari", "HR"),
    ("sari", "Micbiology"),
    ("bishwa", "software developer"),
    ("mina", "Micbiology"),
    ("rita", "HR"),
    ("sachin", "Micbiology"),
    ("gita", "HR"),

]

### Find all from Micbiology department
departname = input("Enter Department Name : ")
nameList = [name for name in name if name[1] == departname]

print(nameList)