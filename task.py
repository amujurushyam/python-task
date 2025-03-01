# # task-1
# # easy ---------level
# # 1. Problem : Write a program to check if a given number is positive, negative, or zero.
# num=float(input("enter a number:"))
# if num > 0 :
#     print("it is a positive number")
# elif num < 0 :
#     print("it is a negative number")
# else :
#     print("it is a zero")

# # 2. Problem : Determine if a number is odd or even.
# num1=float(input("enter a number:"))
# if num1 % 2 == 0:
#     print("even number")    
# else:
#     print("odd number")

# # 3.Check if a person is eligible to vote (age >= 18).

# age=int(input("enter age:"))
# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# # 4.Write a program to find the greatest of two numbers.
# num1=float(input("enter number 1 :"))
# num2=float(input("enter number 2 :"))

# if num1 > num2 :
#     print("number 1 is greater")
# elif num2> num1 :
#     print("number 2 is greater")
# else:
#     print("both are equal")

# # 5.Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."
# num=int(input("enter marks:"))
# if num >= 40 :
#     print("pass")
# else:
#     print("fail")

# # 6.Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
# day_number = int(input("Enter a number (1-7): "))
# days_of_week = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }
# print(days_of_week.get(day_number, "Invalid input. Please enter a number between 1 and 7."))

# #  7. simple calculator
# opt=input("Enter the operation: ").lower()
# a=float(input("Enter the number: "))
# b=float(input("Enter the number: "))
# if opt=="add":
#     print(a+b)
# elif opt=="sub":
#     print(a-b)
# elif opt=="mul":
#     print(a*b)
# elif opt=="div": # division by zero is not possible
#     str1= "division by zero is not possible" if b==0 else print(a/b)
#     print(str1)
# else:
#     print("Invalid operation")  
# print("Thank you for using calculator")

# # 8.Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
# month_number = int(input("enter a number (1-12):"))
# months_in_year = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# print(months_in_year.get(month_number, "Invalid input. Please enter a number between 1 and 12."))

# # Medium --------level

# # 1.Write a program to find the greatest of three numbers.
# shyam_age=int(input("Enter the age: "))
# sumanth_age=int(input("Enter the age: "))
# vamsi_age=int(input("Enter the age: "))
# if shyam_age>sumanth_age and shyam_age>vamsi_age:
#     print("Shyam is elder")
# elif sumanth_age>shyam_age and sumanth_age>vamsi_age:
#     print("Sumanth is elder")
# elif vamsi_age==shyam_age and vamsi_age==sumanth_age:
#     print("All are equal")
# else:
#     print("Vamsi is elder")

# # 2.Check if a year is a leap year.
# # non century years should be divisible by 4
# # century years should be divisible by 400

# year = int(input("Enter the year: "))
# if year % 100 != 0 and year % 4 == 0:
#     print("Leap year")
# elif year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# year = int(input("Enter the year: "))
# if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# # using ternary operator
# print("Leap year") if year % 100 != 0 and year % 4 == 0 or year % 400 == 0 else print("Not a leap year")

# # 3.Write a program to classify a character entered by the user as a vowel, consonant, or neither.
#  str1 = input("Enter a character: ").lower()
# if str1 in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# str1 = input("Enter a character: ").lower()
# if len(str1) > 1 or len(str1) == 0:
#     print("Invalid input")
# else:
#     if str1 in "aeiou":
#         print("Vowel")
#     elif str1.isalpha():
#         print("Consonant")
#     else:
#         print("Neither")
# # use isalpha to check if the input is a letter or not
# # use isdigit to check if the input is a digit or not
# # use isalnum to check if the input is a letter or a digit or not

# # 4.Calculate the grade of a student based on the marks they score:
# # 1. 90-100: Grade A
# # 2. 80-89: Grade B
# # 3. 70-79: Grade C
# # 4. <70: Fail.

# num=int(input("enter marks scored :"))
# if num >= 90 and num < 100:
#     print("Grade A")
# elif num >= 80 and num < 89:
#     print("Grade B")
# elif num >= 70 and num < 79:
#     print("Grade C")
# else:
#     print("Fail")

# # 5.Write a program to check if three sides length form a valid triangle.
# side1 = float(input("side 1 :"))
# side2 = float(input("side 2 :"))
# side3 = float(input("side 3 :"))

# # s1+s2 > s3; s3+s1 > s2; s2+s3 > s1

# print("Valid triangle") if side1 + side2 > side3 and side3 + side1 > side2 and side2 + side3 > side1 else print("Invalid triangle")


# # surprise test-1---------------------------------------------------------------
# # 1. A wizard gives you a magic number and asks you to guess if 
# # it’s divisible by 3 and 5. If it is, print "FizzBuzz". 
# # If it’s only divisible by 3, print "Fizz". If it’s only 
# # divisible by 5, print "Buzz". Otherwise, print the number itself.

# # num=int(input("enter a number :"))3.2
# # if num % 3 == 0 and num % 5 == 0:
# #     print("FizzBuzz")
# # elif num % 3 == 0:
# #     print("Fizz")
# # elif num % 5 == 0:
# #     print("Buzz")
# # else:
# #     print("Invalid")

# # 2.Input health and attack power of both warriors
# # health1 = int(input("enter health 1 :"))
# # attack1 = int(input("enter attack 1 :"))
# # health2 = int(input("enter health 2 :"))
# # attack2 = int(input("enter attack 2 :"))

# # if attack1 > attack2 or (attack1 == attack2 and health1 > health2):
# #     print("Warrior 1 Wins")
# # elif attack2 > attack1 or (attack1 == attack2 and health2 > health1):
# #     print("Warrior 2 Wins")
# # else:
# #     print("Draw")

# # 3.# Input the account balance and withdrawal amount
# # balance = float(input("Enter the account balance: "))
# # withdrawal = float(input("Enter the withdrawal amount: "))

# # if withdrawal % 100 != 0:
# #     print("Amount must be a multiple of 100.")
# # elif withdrawal > balance:
# #     print("Insufficient balance.")
# # else:
# #     balance -= withdrawal
# #     print("Transaction Successful. Remaining balance:", balance)

# # print("Transcation Succesful") if (withdrawal % 100 == 0) and (withdrawal <= balance) else print("appropriate reason")


# # 4.# Input password from the user
# # password = input("Enter a password: ")

# # # Check the length of the password and categorize strength
# # if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "@#$" for c in password):
# #     print("Strong")
# # elif len(password) >= 6 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
# #     print("Medium")
# # else:
# #     print("Weak")

# # 5.# Input three sides of a triangle
# a, b, c = map(float, input("Enter three sides of a triangle: ").split(","))

# # Check if the sides form a valid triangle
# if a + b > c and a + c > b and b + c > a:
#     # Determine the type of triangle
#     if a == b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("Not a Triangle")


# # using functions --------- print even or odd

# # def even_or_odd (x):
# #     if x % 2 == 0:
# #         return "even"
# #     else:
# #         return "odd","even or odd", "edo okati"

# # def void_exmp():
# #     print("hi pandu")


# # res = even_or_odd(11)
# # print(res)
# # print(void_exmp())


# # using functions -------------- print prime

# # def check_if_prime(num1):
# #     if num1 <= 1:
# #         return False
# #     for i in range(2,num1):
# #         if num1 % i == 0:
# #             return False
# #     return True

# # input_num = int(input(" enter number to check if prime or not : "))

# # function_res = check_if_prime(input_num)

# # print(input_num,"is prime") if function_res else print (input_num,"not a prime")


# # using functions ----------------- armstrong in range
# # function1---- we can print a function which checks if a given number is armstrong number . call this for all the numbers in the range
# # function2---- function acccepts lower boud and upper bound and directly prints all numbers in the range.

# # def check_if_armstrong(num1):
# #     # implement the logic here
# #     temp = num1
# #     res =0
# #     while temp > 0:
# #         rem = temp % 10
# #         res += rem ** len(str(num1))
# #         temp = temp // 10

# #     return res == num1

# # lower_bound = int(input("enter the lower bound :"))
# # upper_bound = int(input("enter the upper bound :"))


# # for i in range (lower_bound,upper_bound + 1):
# #     # now i will call a function to check if it is armstrong number 
# #     if check_if_armstrong(i):
# #         print(i)


# # second way 

# def print_armstrong_in_range(lower_bound, upper_bound):
#     for i in range(lower_bound, upper_bound + 1):
#         # implement the logic
#         temp = i
#         res = 0
#         while temp > 0:
#             rem = temp % 10
#             res += rem ** len(str(i))
#             temp = temp // 10
#         if res == i:
#             print(i)

# # Example usage
# lower_bound = int(input("enter the lower bound: "))
# upper_bound = int(input("enter the upper bound: "))
# print_armstrong_in_range(lower_bound, upper_bound)

# # # fibanoci series
# # # f(n) = f(n-1) + f(n-2)
# # # f(0) = 0 , f(1) = 1

# # # input_num = int(input("Enter number of fib needed :"))

# # n1 = 0
# # n2 = 1

# # print(n1)
# # print(n2)

# # for i in range(0,10):
# #     temp = n1 + n2
# #     n1 = n2 
# #     n2 = temp
# #     print(temp)

# num1 = int(input("enter armstrong number"))

# temp = num1

# lower_range = 100
# upper_range = 999

# for i in range (lower_range,upper_range + 1):
#     temp = i


# sum = 0    
# while temp > 0:
#         rem = temp % 10
#         print(rem)
#         sum += rem ** 3
#         temp = temp // 10
# print("Armstrong") if sum == num1 else print ("not")


# compare first digit and last digit in a number  (print equal - if there are  equal )

# ef compare_first_last_digit(num):
#     str1 = str(num)
#     if str1[0] == str1[-1]:
#         print("Equal")
#     else:
#         print("Not equal")

# num = int(input("Enter a number: "))
# compare_first_last_digit(num)  


# reverse of negative numbers 

def reverse_number(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return -int(str(n)[:0:-1])

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))


# search of number in list with their indexes if found 

def search_a_num(list, search_num):
    """Search for a number in the list and print its index."""
    index = 0  
    for num in list:
        if num == search_num:
            return index  
        index += 1  
    return -1  

list = [2, 4, 6, 8, 10, 0.2, -3]
search_num = float(input("Enter a number to search: "))  

index = search_a_num(list, search_num)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")






