weight = 4.5
groundcost = 0.00

#Ground Shipping
if weight <= 2:
  groundcost = 20 + weight*1.50
elif weight <= 6:
  groundcost = 20 + weight*3.00
elif weight <= 10:
  groundcost = 20 + weight*4.00
else:
  groundcost = 20 + weight* 4.75

print("The ground shipping cost is: $" + str(groundcost) + "0")

#Premium Ground Shipping
premium_cost = 125.00
print("The premium shipping cost is: $" + str(premium_cost) + "0")

#Drone Shipping
drone_cost = 0
if weight <= 2:
  drone_cost = weight*4.50
elif weight <= 6:
  drone_cost = weight*9
elif weight <= 10:
  drone_cost = weight*12.00
else:
  drone_cost = weight*14.25
print("The drone shipping cost is: $" + str(drone_cost))

a = groundcost
b = premium_cost
c = drone_cost

if a < b and a < c:
  leastcost = a
  shipping = "Ground Shipping"
if b < a and b < c:
  leastcost = b
  shipping = "Ground Shipping Premium"
if c < a and c < b:
  leastcost = c
  shipping = "Drone Shipping"
print()
print("The cheapest of all 3 shippings is: " + shipping + " at $" + str(leastcost)) 
