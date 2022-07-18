print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

counter = 0
order = ""
lastOrder = ""
orderHistory = {}

while(order != "quit"):
    order = input("> ")

    if(order != "quit"):
        if(order in orderHistory):
            counter+=1
            orderHistory[order] += 1
            print(f" ** {orderHistory[order]} orders of {order} have been added to your meal ** ")
        else:
            counter += 1
            orderHistory[order] = 1
            print(f" ** {orderHistory[order]} order of {order} have been added to your meal ** ")
            lastOrder = order

print("""
***********************************
***       Order Summary         ***
***********************************
""")

for item in orderHistory:
    if(orderHistory[item] > 1):
        print(f"** {orderHistory[item]} orders of {item} **")
    else:
        print(f"** {orderHistory[item]} order of {item} **")

print(f"""
***********************************
***       Total: ${counter}.00        ***
***********************************
""")