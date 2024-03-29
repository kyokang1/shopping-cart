# shopping_cart.py

import os
import csv
from pprint import pprint
import datetime

# TODO: write some Python code here to produce the desired output


##
## Challenges
##

#1. Funtional Challenge - Separate data from the source code
products = []
filepath = os.path.join(os.path.dirname(__file__), ".", "data", "shopping_cart_data.csv")

with open(filepath, "r") as data:
    reader = csv.DictReader(data)
    for row in reader:
        row["price"] = float(row["price"])  # update str to float of price
        products.append(dict(row))

#2. Automated Testing Challenges - Test price format
def to_usd(price):  
    return "${0:,.2f}".format(price)

#breakpoint()


if __name__ == "__main__":

    ##
    ## 1. Capturing User Inputs
    ##
    
    possible_ids = [p["id"] for p in products]
    #print(possible_id) 
    #print(type(possible_id))
    
    selected_ids = []
    selected_prods = []
    total_price = 0
    
    #Greeting
    print("") 
    print("===============================================") 
    print("LET'S START YOUR SHOPPING!!") 
    
    while True:
    
        selected_id = input("Please input a product identifier, or 'DONE': ")
        #print(selected_id)
        #print(type(selected_id))
    
        if selected_id == "DONE": # if DONE, break the loop
            break
        elif selected_id == "":
            print("No input. Please input a product identifier!") # if no input, ask to input
            continue
        elif selected_id not in str(possible_ids):
            print("We cannot find the product. Please try again!") # if invalid input, ask to input again
            continue
    
        matching_prods = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_prod = matching_prods[0]
        
        #print(matching_prods)
        #print(type(matching_prods))
        #print(matching_prod)
        #print(type(matching_prod))
        #print("Selected Product: " + matching_prod["name"] + " // " + str(matching_prod["price"]))   
    
        total_price = total_price + float(matching_prod["price"])
    
        #matching_name = matching_prod["name"]
        #matching_price = matching_prod["price"]   
        #matching_prods2 = [{"name": matching_name, "price": matching_price}]
    
        selected_ids.append(selected_id)
        #selected_prods.append(matching_prod["name"])
        #selected_prods = matching_prod["name"]
    
        selected_prods.append(matching_prod)
    
    
    ##
    ## 2. Look-up Products
    ##
    
    print("") 
    print("===============================================") 
    print("Your Selected Items: ", end='') 
    print(selected_ids)
    
    #print(selected_prods)
    
    for p in selected_prods:
        price_usd = " ... Price: ${0:.2f}".format(p["price"])
        print (" + " + p["name"] + str(price_usd))
    
    print("-----------------------------------------------") 
    print("TOTAL PRICE (BEFORE TAX): " + str(total_price))
    print("PLEASE FIND YOUR RECEIPT BELOW") 
    
    
    ##
    ## 3. Printing the Receipt
    ##
    
    print("") 
    print("===============================================") 
    
    #Store information
    print("CUSTOMER RECEIPT") 
    print("K-YOUNG'S 'ALL-IN-ONE' GROCERY STORE") 
    print("www.kyoungkang.com  // (212)-444-4444") 
    
    #Checkout time
    print("-----------------------------------------------") 
    now = datetime.datetime.now()
    print("CHECK-OUT: " + str(now.strftime("%Y/%m/%d  %H:%M:%S"))) 
    
    #Selected items & price in USD format
    print("-----------------------------------------------") 
    print("SELECTED PRODUCTS:") 
    
    for p in selected_prods:
        price_usd = " ...... ${0:.2f}".format(p["price"])
        print ("   " + p["name"] + str(price_usd))
    
    #Before & After Tax
    def tax_ny(amt):
        return amt * 0.0875
    def after_tax(amt):
        return amt * 1.0875
    
    print("-----------------------------------------------") 
    print("SUBTOTAL: " + str("${0:.2f}".format(total_price)))
    print("TAX (NY 8.75%): " + str("${0:.2f}".format(tax_ny(total_price))))
    print("TOTAL: " + str("${0:.2f}".format(after_tax(total_price))))
    
    #Thank you comment
    print("-----------------------------------------------") 
    print("THANK YOU FOR SHOPPING AT KYOUNG'S!")
    print("") 
    print("===============================================") 
    print("") 
    