# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest 
# and how much it will cost to ship their package using Sal’s Shippers.

weight = 41.5

# Ground Shipping

flat_charge_ground = 20.00
if weight <= 2:
  price_per_pound = 1.50
elif weight <= 6:
  price_per_lb = 3.00
elif weight <= 10:
  price_per_lb = 4.00
else:
  price_per_lb = 4.75
  
cost_ground = flat_charge_ground + weight * price_per_lb
print("Ground Shipping: $",cost_ground)

# Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium: $",cost_ground_premium)

# Drone Shipping
flat_charge_drone = 0.00
if weight <= 2:
  price_per_lb = 4.50
elif weight <= 6:
  price_per_lb = 9.00
elif weight <= 10:
  price_per_lb = 12.00
else:
  price_per_lb = 14.75

cost_drone = flat_charge_drone + weight * price_per_lb
print("Drone Shipping: $",cost_drone)
