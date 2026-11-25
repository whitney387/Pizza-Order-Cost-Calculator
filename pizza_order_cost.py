
# Calculating the total costs of a pizza order

# Prompt the user for inputs:
#       Pizza size (small $8 or large $12) use if
#       Number of toppings $1
#       Delivery distance in miles  (use if)
# Calculate the cost of toppings.
# Calculate the delivery fee.
# Sum up the total cost.
# cost= base_cost+ toppings+ delivery_fee
print('hello world')

#prices
small_price=8
large_price=12
topping_price=1
base_delivery=2
base_delivery_miles=5
extra_mile_fee=1


#input
size=input("Kindly indicate `small` or `large`:").lower()
topping= int(input('How many toppings:'))
radius_in_miles=int(input("How far do you live in miles?:"))

#base cost

if size =='small':
 base_cost=small_price
elif size=='large':
 base_cost=large_price
else:
 print('choose a size among the two')
 raise SystemExit 

#topping
topping_cost=topping_price*topping

# delivery fee

if radius_in_miles==0:
 delivery_fee=0
elif radius_in_miles<=base_delivery_miles:
 delivery_fee=base_delivery
else: 
 extra_miles=radius_in_miles-base_delivery_miles
 delivery_fee=base_delivery_miles+extra_miles*extra_mile_fee
 
#total cost

total_cost=topping_cost+base_cost+delivery_fee

print(f'the final cost is ${total_cost}')
