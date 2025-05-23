import json
from datetime import datetime


while True:
    print("Welcome to tip calculator")
    try:
        table_number = int(input("Enter the table number:\n"))
        bill_amount = float(input("Enter the bill amount:\n"))
        tip = float(input("What percentage of bill you want to tip:\n"))
    except ValueError :
        print("Please enter a valid input")
        continue
    
    bill_without_tax = bill_amount+(tip*bill_amount/100)
    #Below we are adding local food tax which is 5%
    local_tax = 5*bill_without_tax/100
    total_bill = bill_without_tax + local_tax
    try:
        no_of_people = int(input("In how many people you want to split the bill:\n"))
    except ValueError:
        print("No. of people must be an integer")
        continue
    if no_of_people<=0:
        print("number of people must be greter than zero")
        continue
    after_split = total_bill/no_of_people
    print()
    print()
    print()
    
    record  = {
        "timestamp" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "table_number" :table_number,
        "bill_amount" : bill_amount,
        "tip_amount" : tip,
        "total_bill" : round(total_bill,2),
        "no_of_people" : no_of_people,
        "amount_per_person" : round(after_split,2)
        }


    filename = "bill_records.json"

    # Load existing data or start a new list
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Append new record
    data.append(record)

    # Save it back
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)





    print("----Bill Summary----")
    #below we are formating or rouding off(but it will return the float value) the after split amount upto 2 decimals
    #we can do that with round method as well
    print(f"Total bill without tax for table no. {table_number} is ${bill_without_tax:.2f}")
    print(f"local food tax on bill is ${local_tax:.2f}")
    print(f"Total bill for table no. {table_number} is ${total_bill:.2f}")
    print(f"Bill amount for each person is ${after_split:.2f}")
    print()
    print()
    print("---Thank you----")
    print()
    print()
    #the below part of the code will help us to get rid from the infinite loop
    #The .strip() method in Python is a built-in string function used to remove leading and trailing characters from a string
    more_calculation = input("Do you want to calculate more bills\nyes/no:\n").strip().lower()
    if more_calculation == "yes":
        continue
    elif more_calculation =="no":
        break
    else:
        print("Not a valid input ")