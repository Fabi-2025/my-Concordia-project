#Tip calculator: this program calculates the price per person for a meal

diners = int(input("How many diners did you have?"))
meal_price = float(input("How much was the diner?"))
GST = 0.05 #Federal tax
QST = 0.0975 #Regional tax
meal_price_GST = meal_price * GST
meal_price_QST = meal_price * QST
total =meal_price + meal_price_GST +meal_price_QST
print("The GST added is $",meal_price_GST)
print("The QST added is $", meal_price_QST)
print(f"The total of your diner including taxes is ${total:.2f}")
print("1) Exceptional 20%, 2)Good 15%, 3) Basic 10%, 4)Horrible 0%")
tip = input("Please select the tip you would like to give: ")

#This loop will keep asking the user to enter a number as long as the number is not between 1-4.
while tip '1','2','3','4',q'):
    if tip == q:
        print("Bye")
     #print("Please select the tip you want to give (type 1, 2, 3 or 4): ")
     #tip = int(input("Please select the tip you would like to give: "))
    tip = int(tip)
if tip == 1:
    tip_percentage = 0.02
    tip_amount = meal_price *tip_percentage
    print("The tip amount is $", tip_amount, "***Thank you!****")
elif tip == 2:
    tip_percentage = 0.015
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount, "***Thank you!****")
elif tip == 3:
    tip_percentage = 0.01
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount, "***We will improve next time****")
elif tip == 4:
    tip_percentage = 0.0
    tip_amount = meal_price * tip_percentage
    print("The tip amount is $", tip_amount, "***Sorry! Hope you come back****")

grand_total = total + tip_amount
print("The total of your diner including tip is $", grand_total)






#
#
# tip = int(input("What percentage was tipped?"))*0.
# #tip_percent = tip*0.01
# tip = '{:%}'.format(tip)
# print(tip)
# []