# Restaurent Billing System

# veg,non-veg,snacks,sweet-dish

veg={'Yellow_Dal':150,
     'Black_Dal':160,
     'Rice':120,
     'Mixed_Veg':180,
     'Mashroom_Matar':180,
     'Cheese_Tomato':160,
     'Palak_Paneer':190,
     'Mashroom_Cheese':200,
     'Cheese_Potato':120,
     'Roti':5}
nonveg={'Fried_Chicken':450,
        'Simple_Chicken':400,
        'Fried_Fish':350,
        'Egg':20}
snacks={'Cheese_Chilli':150,
        'Burger':70,
        'Pizza':150,
        'Noodles':120,
        'Spring_Rolls':110,}
sweetdish={'Ice_Cream':80,
           'Gulab_Jamun':20,
           'Rasmalai':90}
name=str(input('Enter customer name='))
phone=int(input('Enter customer phone number='))
if(len(str(phone))!=10):
    print('Phone Number is Invalid')
    phone=int(input('Enter valid phone number in 10 Digits='))
address=str(input('Enter the address='))
# Going to give the order'
n=int(input('Enter How many veg iterms ordered by customer='))
if(n>10):
    print('Invalid Option')
    n=int(input('Enter correct number of iterms ordered by customer='))
veg_items=[]
price_veg_items=[]
for x in range(n):
    dish_name=str(input('Enter new dish name='))
    quantity=int(input('Enter the quantity 1 or more='))
    veg_items.append(dish_name)
    price=veg.get(dish_name)
    update_price=price * quantity
    price_veg_items.append(update_price)
m=int(input('Enter How many non veg iterms ordered by customer='))
non_veg_items=[]
price_non_veg_items=[]
for x in range(m):
    dish_name=str(input('Enter new dish name='))
    quantity=int(input('Enter the quantity 1 or more='))
    non_veg_items.append(dish_name)
    price=nonveg.get(dish_name)
    update_price=price * quantity
    price_non_veg_items.append(update_price)
p=int(input('Enter How many snacks iterms ordered by customer='))
snacks_items=[]
price_snacks_items=[]
for x in range(p):
    dish_name=str(input('Enter new dish name='))
    quantity=int(input('Enter the quantity 1 or more='))
    snacks_items.append(dish_name)
    price=snacks.get(dish_name)
    update_price=price * quantity
    price_snacks_items.append(update_price)
s=int(input('Enter How many sweets iterms ordered by customer='))
sweet_dish_items=[]
price_sweet_dish_items=[]
for x in range(s):
    dish_name=str(input('Enter new dish name='))
    quantity=int(input('Enter the quantity 1 or more='))
    sweet_dish_items.append(dish_name)
    price=sweetdish.get(dish_name)
    update_price=price * quantity
    price_sweet_dish_items.append(update_price)
bill_menu={}
for x in range(len(veg_items)):
    bill_menu.update({veg_items[x]:price_veg_items[x]})

for x in range(len(non_veg_items)):
    bill_menu.update({non_veg_items[x]:price_non_veg_items[x]})

for x in range(len(snacks_items)):
    bill_menu.update({snacks_items[x]:price_snacks_items[x]})

for x in range(len(sweet_dish_items)):
    bill_menu.update({sweet_dish_items[x]:price_sweet_dish_items[x]})

# Print the bill menu
print()
print('Bill Menu Of Ordered dish along with price including quanity')
print(bill_menu)

# calculate and print the bill GST 18 %
bill=0
for x in bill_menu:
    p=bill_menu.get(x)
    bill=bill+p
print()
print('Final Bill Without GST=',bill)
gst=bill * 0.18
total_bill=bill+gst
sgst=gst//2
cgst=gst//2

# print Bill SLIP
print("Name=",name)
print('Phone=',phone)
print('Address=',address)
for x in bill_menu:
    print('Dish Name=',x,' Price=',bill_menu[x])
print('Total Bill Without GST=',bill)
print('18% GST on bill=',gst)
print('CGST=',cgst)
print('SGST=',sgst)
print('Total Bill including GST=',total_bill)