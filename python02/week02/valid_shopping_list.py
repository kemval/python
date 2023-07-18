#define available items in the shop
available_items = ('Legos', 'Lamps', 'Leds', 'Mouse')

#define empty lists
shopping_list = []
check_list = []

#function to fill shopping list
def fill_shopping_list(lst, num):
    print("Enter the items you want to add to the shopping list:")
    for num in range(num):
        item = input("Item: ").title()
        lst.append(item)

#function to validate items in shopping cart
def validate_shopping_cart(cart, available):
    return [item for item in cart if item in available]

#ask the user for the number of items
num_items = int(input("How many items do you want to add to the shopping list? "))

#fill the shopping list
fill_shopping_list(shopping_list, num_items)

#validate the items in the shopping cart
check_list = validate_shopping_cart(shopping_list, available_items)

#check
if set(shopping_list) == set(check_list):
    print("All the items in your list are valid. Proceed to checkout.")
else:
    invalid_items = list(set(shopping_list) - set(check_list))
    print("Invalid items:", invalid_items)
    valid_items = list(set(check_list))
    print("Valid items that may be check out:", valid_items)
