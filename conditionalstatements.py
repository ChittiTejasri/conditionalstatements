                                  # if-else:
#check whether the given number is a 3-digit number
# n=int(input("Enter a number: "))
# if n >= 100 and n <= 999:
#     print(n,"it is a 3 digit number ")
# else:
#     print(n,"it is not a 3 digit number")

#check whether given number is divisible by both 3 and 5 or not
# n=int(input("Enter a number:"))
# if n % 3 == 0 and n % 5 == 0:
#     print(n,"it is divisible by 3 and 5")
# else:
#     print(n,"it is not divisible by 3 and 5 ")

#check whether the given traingle is valid traingle or not
# a=int(input("Enter side 1: "))
# b=int(input("Enter side 2: "))
# c=int(input("Enter side 3: "))
# if a + b > c and b + c > a and c + a > b:
#     print("valid Traingle")
# else:
#     print("Invalid traingle")

#check whether a given number is a multiple of 10 or not
# n=int(input("Enter a number:"))
# if n % 10 == 0:
#     print(n,"it is multiply by 10")
# else:
#     print(n,"it is not multiply by 10")

                           #if-elif-else:
#check the type of traingle based on its sides.
#Equilateral,isosceles,or scalene
# a=int(input("Enter side 1:"))
# b=int(input("Enter side 2:"))
# c=int(input("Enter side 3:"))
# if a == b and b == c:
#     print("Equilateral Traingle")
# elif a == b or b == c or a == c:
#     print("Isosceles Traingle")
# else:
#     print("scalene Traingle")

#Calaculate the electricity bill based on units consumed
       #0-100:2/unit,101-200:3/unit,201-300:5/unit,above 300:7/unit.
# units=int(input("Enter electricity bill:"))
# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = units * 3
# elif units <= 300:
#     bill = units * 5
# else:
#     bill = units * 7
# print("Electricity bill ",bill)

#display the age category.
    #Below 13 -Child,13-19-Teenager,20-59-Adult,60 and above - Senior citizen
# age=int(input("Enter a age:"))
# if age < 13:
#     print("Child")
# elif age <= 19:
#     print("Teenager")
# elif age <= 59:
#     print("Adult")
# else:
#     print("Senior Citizen")
#Calculate the discount based on shopping amount.
          #Below 1,000-No discount
          #1000-4999-10%
          #5000-9999-20%
          #10000 and above-30%.
# amount=float(input("Enter shopping amount:"))
# if amount < 1000:
#     discount = 0
# elif amount < 5000:
#     discount = 10
# elif amount < 10000:
#     discount = 20
# else:
#     discount = 30

# discount_amount = amount * discount / 100
# final_discount = amount - discount_amount

# print("Discount = ",discount,"%")
# print("discount amount ",discount_amount)
# print("Final discount ",final_discount)

#Display the season based on the month number.
         #3-5-spring
         #6-8-summer
         #9-11-Autumn
         #12/1/2-winter.
# month=int(input("Enter a season:"))
# if month == 3 or month == 4 or month == 5:
#     print("Spring")
# elif month == 6 or month == 7 or month == 8:
#     print("Summer")
# elif month == 9 or month == 10 or month == 11:
#     print("Autumn")
# elif month == 12 or month == 1 or month == 2:
#     print("Winter")
# else:
#     print("Invalid month") 

#Check whether a given year is a Leap year or not
         #condition 1:Year % 400 == 0
         #condition 2:Year % 4 == 0 and year % 100 !=0
# leapyear=int(input("Enter a year:"))
# if leapyear % 400 == 0:
#     print("Leap year")
# elif leapyear % 4 == 0 and leapyear % 100!= 0:
#     print(" leapyear")
# else:
#     print("Not a Leap Year")

                      #Nested if statements
#Check whether a person is eligible to donate blood
       #Age should be between 18 and 60.
#if eligible by age,weight should be above 50kg.

# age=int(input("Enter age:"))
# if age >= 18 and age <= 60:
#     weight=float(input("Enter a weight in kg:"))

#     if weight > 50:
#         print("Eligible to donate blood")
#     else:
#         print("Not eligible")

#Display the grade based on average only if the student has passed in all 4 subjects
# m1=int(input("Enter marks subject 1:"))
# m2=int(input("Enter marks subject 2:"))
# m3=int(input("Enter marks subject 3:"))
# m4=int(input("Enter marks subject 4:"))

# if m1 >= 35 and m2 >= 35 and m3 >= 35 and  m4 >= 35:
#     Average = m1+m2+m3+m4/4

#     print("Average = ",Average)

#     if Average >= 90:
#         print("Grade A")
#     elif Average >= 75:
#         print("Grade B")
#     elif Average >= 60:
#         print("Grade C")
#     elif Average >= 50:
#         print("Grade D")
#     else:
#         print("Grade E")
# else:
#     print("Failed")

#Check whether a student is eligible for a scholarship.
#Age should be above 18.if eligible by age,score should be above 86
# age=int(input("Enter age:"))

# if age >= 18:
#     score=int(input("Enter score :"))

#     if score >= 86:
#         print("Eligible for Scholarship")
#     else:
#         print("Not eligible")
# else:
#     print("Not eligible")


                                    #While loops
#Find the sum of digits in a given number.
#Example:738-7+3+8=18
# n=738
# sum=0
# while n!=0:
#     ld=n%10
#     sum = sum + ld
#     n= n // 10
# print("Sum of digits = ",sum)

#Find the average of digits in a given number  
#Example:624-(6+2+4)/3=4
# n = 624

# sum = 0
# count = 0

# while n != 0:
#     ld = n % 10
#     sum = sum + ld
#     count = count + 1
#     n = n // 10

# average = sum / count

# print("Average of digits =", average)

#Find the sum of the first digit and the last digit of a given number.
#Example:936-9+6=15
# n=936

# last = n % 10

# while n >= 10:
#     n = n // 10
# first = n

# sum = first + last
# print("Sum of first and last = " ,sum)

#Find the Average of digits that are divisible by 5 in a given number.
#Example 12575-Divisible by 5 digits:5,5_Average=(5+5+5)/3=5
# n=12575
# sum=0
# count=0
# while n!=0:
#     ld = n % 10

#     if ld % 5 == 0:
#         sum = sum + ld
#         count = count + 1
#     n = n // 10

#     average = sum / count
# print("Average of digits divisible by 5 = ",average)

#Find the differencebetween the largestdigitand the smallest digitin a given number.
#Example:58321-Largest=8,smallest=1-Difference=8-1=7
n = 58321
large = 0
small = 9

while n != 0:
    ld = n % 10

    if ld > large:
        large = ld

    if ld < small:
        small = ld

    n = n // 10

difference = large - small

print("Largest digit =", large)
print("Smallest digit =", small)
print("Difference =", difference)



    
    