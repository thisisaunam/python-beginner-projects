# taking input of how many items user wants to purchase
number = int(input("hello!! \nhow many items do you want to buy?: "))

# empty list to input items user is purchasing
item_name = []
item_cost = []
item_quantity = []
item_total = []

# rule system if there are more than 10 items
def get_ordinal(n):
    if 10 <= n % 100 <= 20:
        return f"{n}th"
    elif n % 10 == 1:
        return f"{n}st"
    elif n % 10 == 2:
        return f"{n}nd"
    elif n % 10 == 3:
        return f"{n}rd"
    else:
        return f"{n}th"

# looping input menu to get input according to number of items user wishes to purchase
for i in range (number):
    name = input("\nwhat item do you wish to buy?: ") # name of the item
    cost = float(input("cost of the item you're buying (in $)?: ")) # cost of the item
    quantity = int(input("what quantity do you wish to purchase?: ")) # quantity of the item
    total = cost * quantity
    # appending each item to their list
    item_name.append(name)
    item_cost.append(cost)
    item_quantity.append(quantity)
    item_total.append(total)

bill = 0
# printing each list
for j in range (number):
    label = get_ordinal(j + 1)
    print(f"\n{label} item")
    print ("\t-> name of the item:", item_name[j])
    print ("\t-> cost of the item:", item_cost[j])
    print ("\t-> quantity of the item:", item_quantity[j])
    print ("\t-> total of the item:", f"${item_total[j]:,.2f}\n\n")
    bill += item_total[j]

print(f"""\nokay!
now, your bill is: ${bill:,.2f}""")
print ("\nthank you for purchasing!")
