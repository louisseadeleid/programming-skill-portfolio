#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:48:20 2024

@author: winsicheng
"""

import sqlite3 #IMPORT AND CONNECT THE CODE TO DATABASE

def create_database(): #THIS LINE CREATES A FUNCTION THAT WOULD BE RESPONSIBLE IN CREATING THE DATABASE TABLE
    conn = sqlite3.connect('venmac.db') #THIS CONNECTS THE SQLITE DATABASE FILE 'venmac.db' TO THE CODE
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vending_machine_items (
            code TEXT PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER,
            category TEXT
        )
    ''')

    conn.commit() # MAKES THE CHANGES MADE TO THE DATABASE
    conn.close() #THIS CLOSES THE DATABASE

def populate_database(): # MAKES THE FUNCTION WITH THE MENU OF THE ITEMS NEEDED IN THE VENDING MACHINE
    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()

    items_data = [ #DEFINES THE LIST OF ITEMS THAT THERE IS IN THE VENDING MACHINE WITH THE TUPLE REPRESENTING ITS CODE, NAME, QUANTITY, AND CATEGOORY
    ('A1', 'Coke', 2.50, 8, 'Soft Drinks'),
    ('A2', 'Sprite', 2.50, 6, 'Soft Drinks'),
    ('A3', 'C2 Iced Tea', 3.50, 12, 'Beverages'),
    ('A4', 'Cool Sun Apple Juice', 2.50, 12, 'Beverages'),
    ('A5', 'Water', 1.00, 8, 'Water'),
    ('A6', 'Red Bull', 3.00, 10, 'Energy Drinks'),
    ('A7', 'Monster Energy', 3.50, 10, 'Energy Drinks'),
    ('A8', 'Lipton Ice Tea', 2.00, 12, 'Beverages'),
    ('A0', 'Nestea Lemon', 2.00, 12, 'Beverages'),

    ('B1', 'Kinder Hippo', 3.50, 12, 'Chocolate'),
    ('B2', 'Kitkat', 4.50, 12, 'Chocolate'),
    ('B3', 'Dairy Milk Hazelnut Chocolate', 4.50, 12, 'Chocolate'),
    ('B4', 'Maltesers', 4.50, 12, 'Chocolate'),
    ('B5', 'Kinder Bueno', 2.00, 15, 'Chocolate'),
    ('B6', 'Milky Way', 1.50, 15, 'Chocolate'),

    ('D1', 'Lays Classic', 2.00, 10, 'Chips'),
    ('D2', 'Doritos Nacho Cheese', 2.50, 10, 'Chips'),
    ('D3', 'Pringles Original', 3.00, 10, 'Chips'),
    ('H1', 'Oreo Cookies', 3.00, 10, 'Cookies'),
    ('H2', 'Digestive Biscuits', 2.50, 10, 'Biscuits'),

    ('C1', 'Buldak Carbonara Cup Noodles', 5.50, 12, 'Noodles'),
    ('C2', 'Yakisoba Chicken Flavor Cup Noodles', 4.50, 12, 'Noodles'),
    ('C3', 'Yakisoba Beef Flavor Cup Noodles', 4.50, 12, 'Noodles'),
    ('C4', 'Jin Ramen Cup Noodles Mild Flavor', 4.50, 12, 'Noodles'),
    ('C5', 'Jin Ramen Cup Noodles Spicy Flavor', 4.50, 12, 'Noodles')
]

    for item in items_data: #CREATES A LOOP FOR THE IHE ITEMS IN THE LIST
        try:
            cursor.execute("INSERT INTO vending_machine_items VALUES (?, ?, ?, ?, ?)", item)
            conn.commit()
        except sqlite3.IntegrityError: #BLOCKS THE POTENTIAL ERRORS IN USER HANDLING 
            print(f"Item {item[0]} already exists.")

    conn.close()

def show_menu(): #THIS PART OF THE CODE RETRIEVES ALL THE ITEM IN THE DATABASE TO SHOW THE USERS
    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vending_machine_items")
    items = cursor.fetchall()

    print("Vending Machine Menu")
    for code, name, price, quantity, category in items:
        print(f"{code}: {name} (AED{price:.2f}) - {quantity} remaining ({category})")

    conn.close()

def get_user_choice(): # THIS FUNCTION GETS THE USER'S ENTRY WHEN THEY ENTER THE CODE THEY WANT TO PURCHASE
    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()
    cursor.execute("SELECT code FROM vending_machine_items") # GETS ALL THE LIST OF ITEM CODES FROM THE DATABASE
    available_items = [item[0] for item in cursor.fetchall()]
    conn.close()

    while True:
        choice = input("Enter item code or simple type 'x' to stop transactios: ")
        if choice.lower() == 'x': # MAKES THE USER ENTER THE INTER CODE AND IF USER ENTERS X THEN THE FUNCTION RETURNS TO NONE INDICATING THAT THEYRE CANCELLING THE PURCHASE
            return None
        if choice in available_items: # IF THE CHOSEN CHOICE IS IN THE AVAILABLE ITES THE FUNCTION RETURNS THE CHOSEN ITEM CODE IF NOT AN ERROR SIGN IS DISPLAYED 
            return choice
        else:
            print("Invalid transaction, Sorry!")

def check_funds(item_code, inserted_money): # CREATES A FUNCTION THAT CHECKS IF THE USER INSERTED ENOUGH MONEY
    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM vending_machine_items WHERE code = ?", (item_code,)) # RETRIEVES AND CHECKS THE PRICES OF THE ITEM
    result = cursor.fetchone()
    conn.close()

    if result:
        item_price = result[0]
        if inserted_money >= item_price: # CHECKS IF THE INSERTED IS ENOUGH AND CALCULATES BUT IF NOT AN ERROR MESSAGE IS DISPLAYED
            return True
        else:
            difference = item_price - inserted_money
            print(f"Not enough money!!. You need AED{difference:.2f} more.")
            return False
    else:
        print("Item not found.")
        return False

def dispense_item(item_code, inserted_money):
    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE vending_machine_items SET quantity = quantity - 1 WHERE code = ?", (item_code,)) #THIS MAKES SURE THE ITEM IS STILL IN STOCK AND UPDATES THE DATABASE THE CURRENT STOCK OF ITEMS IN THE DATABASE WHENEVER SOMEONE MAKES A PURCHASE
    conn.commit()
    conn.close()

    conn = sqlite3.connect('venmac.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price, name FROM vending_machine_items WHERE code = ?", (item_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        item_price, item_name = result
        change = inserted_money - item_price # CALCULATES THE AMOUNT
        print(f"Dispensing {item_name}.")
        if change > 0:
            print(f"Your change is AED{change:.2f}") #CALCULATES THE CHANGE WHENEVER THE INSERTED MONEY IS OVER THE PRICE

def insert_money(): #THIS FUNCTION PROMPTS THE USER TO INSERT MONEY AND HANDLE USER INVALID INPUT OR CANCELLATION
    while True:
        try:
            amount = float(input("Insert money (or type '0' to cancel): AED ")) # THIS GIVES THE USER A CHOICE TO CANCEL PURCHASE
            if amount >= 0:
                return amount
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    create_database() # THESE TWO LINES CALLS THE FUNCTIONS 
    populate_database()

    while True: #INITIATES A LOOP THE WOULD CONTINUE THE MACHINE TO OPERATE UNTIL THE USER CANCELS THE PURCHASE
        money_inserted = insert_money()
        if money_inserted == 0: # GIVES THE USER A CHANCE TO CANCEL PURCHASE AND CANCEL TRANSACTION
            print("Transaction canceled.")
            break

        show_menu() # DISPLAYES THE CURRENT MENU WITHE AVAILABLE ITEM'S CODE, NAME, PRICES, QUANTITY, AND CATEGORY
        user_choice = get_user_choice()

        if user_choice:
            conn = sqlite3.connect('venmac.db')
            cursor = conn.cursor()
            cursor.execute("SELECT quantity FROM vending_machine_items WHERE code = ?", (user_choice,))
            result = cursor.fetchone()
            conn.close() # THESE LINES ESTABLISH THE CONNECTION TO THE DATABASE TO RETRIEVE THE CURRENT STOCK OR QUANTITY OF THE SELECTED ITEM FROM THE DATABASE

            if result and result[0] > 0: # CHECKS IF THERE ARE STILL STOCK 
                if check_funds(user_choice, money_inserted): # CALLS THE FUNCTION TO VERIFY IF THE USER INSERTED ENOUGH MONEY
                    dispense_item(user_choice, money_inserted)
                    break
                else:
                    print("Item out of stock, Sorry!") #MAKES SURE TO NOTIFY USER IF THE ITEM IS OUT OF STOCK
            else:
                print("Item is not here, Sorry!") # OR ELSE IT NOTIFIES THAT THERE IS NO PRODUCT
        else:
            print("Thank you!")
            break

if __name__ == "__main__":
    main()