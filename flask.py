#assignmens  
"""1)You have a list of products in your inventory with their quantities. Write a function to restock an item by adding a specified quantity to it.
    - *Instructions:*
      1. Check if the product exists in the inventory list.
      2. If it exists, update its quantity.
      3. If it doesn't exist, add the product with the given quantity."""

def restock_inventory(inventory,product,quantity):
    for item in inventory:
        if item['name'] == product:
            item['quantity'] = quantity
            return inventory
    inventory.append({'name':product,'quantity':quantity})
    return inventory              

"""2)You have a list of students' grades. Write a function to calculate the median grade.
    - *Instructions:*
      1. Sort the list of grades.
      2. If the number of grades is odd, return the middle grade.
      3. If the number of grades is even, return the average of the two middle grades."""


def calculate_median(grades):
    grades.sort() 
    n = len(grades)
    mid = n // 2
    if n % 2 == 0:
        return (grades[mid - 1] + grades[mid]) / 2
    else:
        return grades[mid]


"""3. *Library System*
    - *Scenario:* You have a list of books in a library system. Write a function to find the most frequently borrowed book.
    - *Instructions:*
      1. Create a dictionary to count the frequency of each book.
      2. Iterate through the list and update the count for each book.
      3. Find and return the book with the highest count."""
def most_frequent_books(books):
    frequency = {}
    for book in books:
        frequency[book] = frequency.get(book, 0 ) + 1
    return max(frequency,key=frequency.get)

"""4)You have a list of students marked present on different days. Write a function to find students who were present on all given days.
    - *Instructions:*
      1. Convert each day's attendance list into a set.
      2. Find the intersection of all sets.
      3. Return the students who are present in all sets."""

def find_present_students(attendance_lists):
    sets = [sets(day) for day in attendance_lists]
    return list(set.intersection(*sets))

"""5)You have a shopping cart represented as a list of items with their prices. Write a function to apply a discount to all items over a certain price.
    - *Instructions:*
      1. Iterate through the list of items.
      2. If an item's price is above the specified limit, apply the discount.
      3. Return the updated list."""

def apply_discount(cart,limit,discount):
    return [{'item': item['item'],'price':item['price'] * 
    (1 - discount/100)} if item['price'] > limit else item for item in cart]
    
    
"""6) You have a list of movie ratings. Write a function to find the top N movies with the highest ratings.
    - *Instructions:*
      1. Sort the list of ratings in descending order.
      2. Return the top N ratings."""

def top_n_movies(ratings,N) :
    ratings.sort(reverse=True)
    return ratings[:N]

"""7)You have a list of customer orders. Write a function to remove orders that are duplicates.
    - *Instructions:*
      1. Create a new list to store unique orders.
      2. Iterate through the original list and add orders to the new list if they are not already present.
      3. Return the list of unique orders."""

def remove_duplicates(orders):
    unique_orders = []
    seen = set()
    for order in orders:
        if order not in seen:
            seen.add(order)
            unique_orders.append(order)
    return unique_orders              

    
         

