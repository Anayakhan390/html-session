#Activity-1-odd even
number=int(input("enter a number :  "))
print("number s :", number)
if number%2==0:
    print("number is even")
else:
    print("number is odd")
#Activity-2-BMI
weight=int(input("enter your weight in kg : "))
height=int(input("enter your height in cm : "))
BMI= weight/(height/100)**2
print("your bmi is :", BMI)

if BMI<18.5:
    print("you are underweight")
elif BMI<18.5 and BMI<24.9:
    print("you are normal")
elif BMI>=25 and BMI<29.9:
    print("you are overweight")
else:
    print("you are obese")

    import datetime
current_time = datetime.datetime.now()
print("Current time is:", current_time)

import calendar
print(calendar.month(2025, 10))

num= int(input("enter a number : "))
if num > 50:
  if  num % 2 == 0:
    print("number is even")
  else:
    print("number is odd")
else : print("number is less than 50")

