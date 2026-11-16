
# Name of the student : Sindhu Kakuru
# Team name : Pysolo 
# Building a menu-driven program for a fictional De Anza College Food Court using functions.
import sys


def show_menu():
    """Display the menu of burger options at the De Anza College Food Court."""
    print(
    """ Welcome to De Anza College Food Court 
    BURGER CLUB OPTIONS
    1. Deanza Burger : 5:25$
    2. Bacon Cheese Burger : 5:75$
    3. Mushroom Swiss : 5.95$
    4. Western Burger : 5.95$
    5. Don Cali Burger : 5.95$
    6. Exit 
    Please make a choice  
    """)


def compute_bill(subtotal,person):
    """This function computes the total bill including tax based on the subtotal and the type of person (staff or student)."""
    # constants for tax rates
    STAFF_TAX_RATE = 0.09
    STUDENT_TAX_RATE = 0.0
    if person == "staff": 
        tax = STAFF_TAX_RATE
    else:
        tax = STUDENT_TAX_RATE
    result = subtotal + (subtotal * tax)
    return result

def match_inputs(food_item):
    """This function matches the user's input to the corresponding burger item and returns its price and name."""
    price = 0
    match food_item:
        case "1": 
            print ("Deanza Burger is a great choice")
            name = "Deanza Burger"
            price = 5.25
        case "2": 
            print ("Bacon Cheese Burger is a good choice")
            name = "Bacon Cheese Burger"
            price = 5.75
        case "3":
            print ("Mushroom Swiss Burger is an excellent choice")
            name = "Mushroom Swiss Burger"
            price = 5.95
        case "4":
            print ("Western Burger is a yummy choice")
            name = "Western Burger"
            price = 5.95
        case "5":
            print ("Don Cali Burger is a delicious choice")
            name = "Don Cali Burger"
            price = 5.95
        case _:
            # The underscore (_) acts as the default 'catch-all' case
            print("\n[Invalid Selection] Please choose a valid option from 1 to 6.")

    return price, name


def print_bill(bill, items_purchased, subtotal):
    """This function prints the final bill for the user."""
    print("=" * 50) # Print a separator line before the bill details
    for item in items_purchased:
        item_total = item["price"] * item["quantity"]
        print(f"{item['quantity']} x {item['name']:<25} ${item_total:.2f}")
    print(f"{'Subtotal:':<38} ${subtotal:.2f}")
    tax_amount = bill - subtotal
    print(f"{'Tax Amount:':<38} ${tax_amount:.2f}")
    print(f"{'Total Amount Due:':<38} ${bill:.2f}")
    print("=" * 50) # Print a separator line after the bill details

def get_input():
    """This function gets input from the user for their choice of burger."""
    try:
        choice = input("Enter your choice of Burger (1-6): ").strip()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit()
    return choice



def main():
    show_menu()
    items_purchased = []
    FLAG = True 
    # Track whether the user has placed any orders
    has_ordered = False 
    while FLAG:
        #Allowing users to place multiple orders before choosing to exit.   
        choice = get_input() 
        if choice in ["1", "2", "3", "4", "5"]:
            price, name = match_inputs(choice)
            quantity = int(input("How many of this burgers do you want: ").strip())
            # List of items purchased, where each item is a dictionary with name, price, and quantity
            items_purchased.append({
                "name": name,
                "price": price,  
                "quantity": quantity
            })   
            has_ordered = True
        elif choice in ["6", "exit", "quit"]:
            FLAG = False
            if has_ordered:
                print ("Thank you, Enjoy your meal!")
            else:
                print ("Thank you, hope to see you again!")
                sys.exit()
        else:
            print("\n[Invalid Selection] Please choose a valid option from 1 to 6.")
    
    # make a subtotal of all items ordered
    subtotal = 0
    for item in items_purchased:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total

    # ask the user if they are a student or staff , based on that we need to determine the tax
    person = input("Are you a student (S) or staff (F): ").strip().lower()
    if person == "s":
        person = "student"
    elif person == "f":
        person = "staff"
    else:
        print("Invalid input. Please enter 'S' for student or 'F' for staff. Try again")
        sys.exit()

    # compute the total bill based on subtotal and person type
    total_bill = compute_bill(subtotal, person)
    print_bill(total_bill, items_purchased, subtotal)
    #help(show_menu)
    #help(get_input)
    #help(match_inputs)
    #help(compute_bill)
    #help(print_bill) 




if __name__ == "__main__":
   main() 


"""
OUTPUTS 
(.venv) (base) sindhukakuru@sindhukakurus-MacBook-Pro D041A 02Y Python Programming % "/Users/sindhukakuru/Desktop/D041A 02Y Python Programming/.venv/bin/python" "/Users/sindh
ukakuru/Desktop/D041A 02Y Python Programming/DO41A_Midterm_part1.py"
 Welcome to De Anza College Food Court 
    BURGER CLUB OPTIONS
    1. Deanza Burger : 5:25$
    2. Bacon Cheese Burger : 5:75$
    3. Mushroom Swiss : 5.95$
    4. Western Burger : 5.95$
    5. Don Cali Burger : 5.95$
    6. Exit 
    Please make a choice  
    
Enter your choice of Burger (1-6): -9

[Invalid Selection] Please choose a valid option from 1 to 6.
Enter your choice of Burger (1-6): 2
Bacon Cheese Burger is a good choice
How many of this burgers do you want: 0
Enter your choice of Burger (1-6): 3
Mushroom Swiss Burger is an excellent choice
How many of this burgers do you want: 9
Enter your choice of Burger (1-6): fdsf

[Invalid Selection] Please choose a valid option from 1 to 6.
Enter your choice of Burger (1-6): 9

[Invalid Selection] Please choose a valid option from 1 to 6.
Enter your choice of Burger (1-6): 6
Thank you, Enjoy your meal!
Are you a student (S) or staff (F): s
==================================================
0 x Bacon Cheese Burger       $0.00
9 x Mushroom Swiss Burger     $53.55
Subtotal:                              $53.55
Tax Amount:                            $0.00
Total Amount Due:                      $53.55
==================================================


(.venv) (base) sindhukakuru@sindhukakurus-MacBook-Pro D041A 02Y Python Programming % "/Users/sindhukakuru/Desktop/D041A 02Y Python Programming/.venv/bin/python" "/Users/sindh
ukakuru/Desktop/D041A 02Y Python Programming/DO41A_Midterm_part1.py"
 Welcome to De Anza College Food Court 
    BURGER CLUB OPTIONS
    1. Deanza Burger : 5:25$
    2. Bacon Cheese Burger : 5:75$
    3. Mushroom Swiss : 5.95$
    4. Western Burger : 5.95$
    5. Don Cali Burger : 5.95$
    6. Exit 
    Please make a choice  
    
Enter your choice of Burger (1-6): 6
Thank you, hope to see you again!
(.venv) (base) sindhukakuru@sindhukakurus-MacBook-Pro D041A 02Y Python Programming % 

(.venv) (base) sindhukakuru@sindhukakurus-MacBook-Pro D041A 02Y Python Programming % "/Users/sindhukakuru/Desktop/D041A 02Y Python Programming/.venv/bin/python" "/Users/sindh
ukakuru/Desktop/D041A 02Y Python Programming/DO41A_Midterm_part1.py"
 Welcome to De Anza College Food Court 
    BURGER CLUB OPTIONS
    1. Deanza Burger : 5:25$
    2. Bacon Cheese Burger : 5:75$
    3. Mushroom Swiss : 5.95$
    4. Western Burger : 5.95$
    5. Don Cali Burger : 5.95$
    6. Exit 
    Please make a choice  
    
Enter your choice of Burger (1-6): 1
Deanza Burger is a great choice
How many of this burgers do you want: 4
Enter your choice of Burger (1-6): 6
Thank you, Enjoy your meal!
Are you a student (S) or staff (F): j
Invalid input. Please enter 'S' for student or 'F' for staff. Try again
(.venv) (base) sindhukakuru@sindhukakurus-MacBook-Pro D041A 02Y Python Programming % 
"""
