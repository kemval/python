item_price = float (input("Enter item price: "))
item_amount = int (input ("How many items are you taking with you?: "))
items_total = float(item_price*item_amount)
sales_tax = float (items_total* 0.13)
descount = float (items_total * 0.10)
final_price = float ((items_total-descount)+sales_tax)
print("Per one item it is going to cost you ", item_price,)
print("you are taking ", item_amount)
print("total before taxes and descount: ", items_total)
print("the extra for taxes is going to be: ", sales_tax)
print("the total of the descount is: ", descount)
print("the total of your purchase is: ", final_price)





