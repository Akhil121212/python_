"""car_types = {'maruthi':'nice','tata':'strong','suzuki': 'fast'}
print(car_types)
for car in car_types:
    print(car,car_types[car])
for key, value in car_types.items():
    print(key,value)    
car_types.pop("tata")
print(car_types) 
car_types.popitem()
print(car_types)

car_types_copy = car_types.copy()
print(car_types_copy)

tea_shop = {
    "chai":{"masala": "spicy", "ginger":"zesty"},
     "tea": {"green":"mild", "black":"strong"}
}

print(tea_shop)

squared_num = {x:x**2 for x in range(20)}
print(squared_num)

#tuples

tea_types = ("Black","green","oolong")
print(tea_types)
print(tea_types[0])
print(len(tea_types))
more_tea = ("herbal","grel")
all_tea = more_tea + tea_types
print(all_tea)
if "green" in all_tea:
    print("i have green tea")
print(all_tea.count("herbal"))    
print(type(tea_types))"""

"""1)age = int(input("Provide me a age:"))

if (age < 13):
    print("children")
elif (age < 20 ):
    print("teenager") 
elif (age < 60):
    print("adult")
else:
    print("senior")"""

"""2)age = int(input("Enter age:"))
day = input("Enter day:")

price = 12 if age >= 18 else 8 
if day == "wednesday":
    price -= 2
print("Ticket price for you is:",price)"""

"""3)Score = int(input("Score:"))

if Score >= 101:
    print("Check your score")
    exit()

if Score >= 90:
    grade = "A"
elif Score >=80:
    grade = "B"
elif Score >= 70:
    grade = "C"
elif Score >= 60:
    grade = "D"
else:
    grade = "F"     

print("Grade is:",grade) """

"""4)fruit = "Banana"
colour = "yellow"

if fruit == "Banana":
    if colour == "green":
        print("Unripe")
    elif colour == "yellow":
        print("Ripe")
    elif colour == "Brown":
        print("OverRipe")"""

weather = input("Weather:")        

if weather == "sunny":
    activity = "go to walk"
elif weather == "rainy":
    activity = "Read a book"
        

