"""1)distance = int(input("distance:"))

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of:",transport)

order_size = "medium"
extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"
print("order:",coffee)        
"""
"""3)password = input("password:")
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("password strength is :",strength)            

year = int(input("year:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")    """

"""5)numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of positive numbers is :",positive_number_count) """

""" 6)n = int(input("n:"))
sum_even = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum_even += 1
print("sum of even numbers is ,",sum_even)        
"""

"""7)number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number, 'x', i, '=',number*i)
"""
"""8)input_str = "Python"
reversed_str = ""
 
for char in input_str:
    reversed_str = char + reversed_str 
print(reversed_str)    """

"""8)input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("char is:",char)
        break
"""
"""9)number = int(input("number:"))
factorial = 1

while number > 0:
    factorial = factorial + number
    number -= 1

print("Factorial:",factorial)    
"""
"""10)while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalide number, try again")    
        """

"""11)number = int(input("Enter number:"))
is_prime = True

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)            
"""

"""12)items = ["apple","banana","orange","apple","mango"]
unique_item  = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    unique_item.add(item)
print(items)    
"""
"""13)import time

)wait_time = 1
max_retries = 10
attempts = 0

while attempts < max_retries:
    print("Attempt",attempts + 1, "-wait time",wait_time)
    time.sleep(wait_time)
    wait_time += 2
    attempts += 1
""" 

"""username = "Akhilesh"

def func():
    username = "Adeeb"
    print(username)

print(username)
func()"""

"""x = 99

def func2(y):
    z = x  + y
    return z
result = func2(1) 
print(result)"""

"""def f1():
    x = 33
    print(x)
    def f2():
        x = 22
        print(x)
    f2()
f1()  """      
i = 0
while(i < 5):
    if i == 2:
        break
    print(i)
    i = i + 1