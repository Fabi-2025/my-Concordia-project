#Tip calculator: this program calculates the price per person for a meal

diners = int(input("How many diners did you have?"))
meal_price = float(input("How much was the diner?"))
GST = 0.05 #Federal tax
QST = 0.0975 #Regional tax
meal_price_GST = meal_price * GST
meal_price_QST = meal_price * QST
total =meal_price + meal_price_GST +meal_price_QST
tip_options = ["1","2","3","4"]

while True: #The code will run within this loop until the tip typed matches the tip_options
    tip_selected = input("Please select the tip you would like to give: "
                    "1) Exceptional 20%, 2)Good 15%, 3) Basic 10%, 4)Horrible 0%")

    #If letter q is typed, then print bye and exit the loop

    if (tip_selected in tip_options):
        break
    print("Input invalid, please select the tip you want to give (type 1, 2, 3 or 4): ")

print(f"You have selected {tip_selected}")
if tip_selected == "1":
    tip_percentage = 0.02
    tip_amount = meal_price *tip_percentage
    print("The tip amount is $", tip_amount, "***Thank you!****")
elif tip_selected == "2":
    tip_percentage = 0.015
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount)
elif tip_selected == "3":
    tip_percentage = 0.01
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount)
elif tip_selected == "4":
    tip_percentage = 0.0
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount)

grand_total = total + tip_amount
print(f"The GST added is ${meal_price_GST:.2f}")
print(f"The QST added is ${meal_price_QST:.2f}")
print(f"The total of your diner including taxes is ${total:.2f}")
print(f"The total of your diner including tip is $ {grand_total:.2f}")


# import pandas as pd
#
# df = pd.read_csv('50000_Sales_Records.csv')
# print(df.head())




#
#
# tip = int(input("What percentage was tipped?"))*0.
# #tip_percent = tip*0.01
# tip = '{:%}'.format(tip)
# print(tip)
# []