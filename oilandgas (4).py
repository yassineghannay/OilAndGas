# Variables
gas_price = 1.07
oil_price = 15.24
discount_rate = 0.90
no_discount_rate = 1
oil_max = 96
gas_max = 4000
GST_5 = 0.05
GST_13 = 0.13
GST_15 = 0.15
five_percent_provinces = ["ab", "bc", "mb", "nt", "nu", "qc", "sk", "yt"]

# Welcome Message
print("---------------------------------------")
print("*** Welcome to Gas Station Program! ***")
print("---------------------------------------")
print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil") 
user_choice = input(">>> ").lower()

if user_choice in ["g", "o"]:
  if user_choice == "g":
      product = "Gas"
      gas_amount = int(input("Enter the number of litres of Gas: "))
      amount = gas_amount
      price = gas_price
      maximum = gas_max
      base_price = gas_amount * gas_price
  elif user_choice ==  "o":
      product = "Oil"
      oil_amount = int(input("Enter # of cases of Oil: "))
      amount = oil_amount * 12
      price = oil_price
      maximum = oil_max
      base_price = oil_amount * oil_price

  province_choice = input("Please enter the 2 letters province abbreviation: ").lower()
  if province_choice in five_percent_provinces:
    tax_rate = GST_5
  elif province_choice == "on":
    tax_rate = GST_13
  else:
    tax_rate = GST_15

  # Calculations
  if amount <= maximum:
    discounted_price = base_price * no_discount_rate
  else:
    discounted_price = base_price * discount_rate

  tax = discounted_price * tax_rate
  final_cost = discounted_price + tax
    
  # Display Results
  print("-------------------------------------------------------------------------------------------------------------------------------------")
  print("Product\t\t# of Liters\t\tPrice before discount\t\tPrice after discount\t\tGST\t\tTotal Price")
  print(f"{product}\t\t{amount}\t\t\t{base_price:.2f}\t\t\t\t{discounted_price:.2f}\t\t\t\t{tax:.2f}\t\t{final_cost:.2f}")
  print("-------------------------------------------------------------------------------------------------------------------------------------")
  print ("Thanks for your business, Good Bye")

else:
  print("Invalid input, you should enter g/G or o/O")
