# First we create our menu list.
# Take our menu items into a dictionary as the key.
# Set the value of remaining stock with the desired key.
# Follow the same steps, but this time setting the value to be the price per product.
# Create an empty dictionary so we can loop through our existing ones.
# Do the math to work out the item value, then save it to a new dictionary.
# Add the individual item totals together to work out the value of the remaining stock.

# Menu list.
menu = ['Coffee',
        'Tea',
        'Pancakes',
        'French Toast']

# Printing the *menu like this allows us to unpack and print the menu as plain text on seperate lines.
print ("The cafe menu:",*menu , sep="\n")
print ("\n")

# Stock dictionary.
stock = {'Coffee':13,
         'Tea':15,
         'Pancakes':27,
         'French Toast':19}

# Because its a dictionary we need it to print differently to show both key(k) and value(v).
# It makes it more neat and presentable to do it this way to see it in a vertical list if we wished to call it.
print ("The stock Inventory:")
for key, value in stock.items():
     print (key, value, sep=": ")
print ("\n")


# Price dictionary.
price = {'Coffee':3.00,
         'Tea':3.00,
         'Pancakes':5.00,
         'French Toast':6.20}

print ("The Price of each item:")
for key, value in price.items():
     print (key, value, sep=": £")
print ("\n")

# Empty item value dictionary.
item_value = {}

# Looking for keys to multiply with and save in a new dictionary.
for key in stock:
    item_value[key] = (stock[key] * price[key])

print ("The remaining value per product:")
for key, value in item_value.items():
     print (key, value, sep=": £")
print ("\n")

# Store value takes all the information added together and saves as a string.
store_value = "{:.2f}".format(item_value['Coffee'] + item_value['Tea'] + item_value['Pancakes'] + item_value['French Toast'])

print ("The overall combined value of remaining inventory:")
print ("£"+store_value)

