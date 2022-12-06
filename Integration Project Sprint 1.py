#Silvana Tellez
#Integration Project Sprint 1
print("Hello user!")
print("Today we will be learning about python3, by going shopping!")
# First we will find some items at the store
num_of_milk= float(input("How many milk cartons are you buying?" " "))
num_of_bread= float (input("How many bags of bread are you buying?" " "))
num_of_eggs= float(input("How many boxes of eggs are you buying?" " "))
#The input function allows the computer to take the input from the user and store it in the variable
#Next we'll find how much each item costs
price_of_milk = 2.50
print("The cost of 1 carton of milk is: $", format(price_of_milk, '.2f'), sep="")
price_of_bread = 1.50
print("The cost of 1 bag of bread is: $", format(price_of_bread, '.2f'), sep="")
price_of_eggs = 3.00
print("The cost of 1 box of eggs is: $", format(price_of_eggs, '.2f'), sep="")
#the format command allws us to concatenate parts of a string
#the '.2f' allows us to have two decimal points in our answer
#Now we find how much is the total price for the amount of items we want
total_price_of_milk = num_of_milk * price_of_milk
print("Total cost of milk is: $", format(total_price_of_milk, '.2f'), sep="")
total_price_of_bread = num_of_bread * price_of_bread
print("Total cost of bread is: $", format(total_price_of_bread, '.2f'), sep="")
total_price_of_eggs = num_of_eggs * price_of_eggs
print("Total cost of eggs is: $", format(total_price_of_eggs, '.2f'), sep="")
#the * numeric operator multiplies the variables together
#the sep= "" makes sure that the $ adn the number don't have a space in between
#Now we'll add all the total item prices with the + operator to get your total cost
total_purchase_cost= total_price_of_milk + total_price_of_bread + total_price_of_eggs
print("Your total before tax will be: $", format(total_purchase_cost, '.2f'), sep="")
#At the register the cashier notices that one of the milk cartons has gone bad
#So we subtract it from the total with the - operator
update_total_purchase_cost = total_purchase_cost - price_of_milk
print("Sorry about that, your total before taxes now is: $", format(update_total_purchase_cost, '.2f'), sep="")
#Now we have to find the taxes
tax_rate= 1.07
total_with_tax = tax_rate * update_total_purchase_cost
print("Your final total with tax is: $", format(total_with_tax, '.2f'), sep="")
#You decide you'll use cash to pay for some of it but you don't have coins
#we use the // operator to get the amount of cash we owe to the closest integer
cash_owed= total_with_tax//4
print("In cash you owe: $", format(cash_owed, '.2f'), sep="")
#now we find what we owe in a card
card_owes= total_with_tax - cash_owed
print("In card you owe: $", format(card_owes, '.2f'), sep="")
#you decide to slpit the amount you owe in card between two cards
#we use the / operator to divide it
card_1_owes = card_owes/2
card_2_owes = card_owes/2
print("Your first card owes: $", format(card_1_owes, '.2f'), sep="")
print("Your second card owes: $", format(card_2_owes, '.2f'), sep="")
#Once you get out of the store you go to your car and it starts beeping 10 times
#we use the * as a string operator
print("Beep!" * 10)


#This is not part of the main program
#We use the end="" argument to add a string after the output of the print statement
print("We can do it!"" ", end="AND")
print(" ""We will do it!")
#The + in a string is puts the two statements together without a space
print("I am 20" + "years old.")
#The ** operator means an exponent
print(2**3)
#the % is called a modulo and its used to get the remainder of the division
print(22%3)
#Sprint 2 Begins Here
#The AND boolean is true if both are true, if is used to determine the conditions
first_num = 3
second_num = 4
if first_num > 1 and second_num > 1:
    print("These are greater than 1!")
#The OR boolean is true if at least one if true, if-else is used to determine the conditions
first_num = 5
second_num = 8
if first_num or second_num > 5:
    print("At least of of the numbers is greater than 5!")
else:
    print("None of the numbers are greater than 5!")
#The NOT boolean is true if it does not meet the condition, if is used to determine the condition
first_num = 3
second_num = 5
if not (first_num == second_num):
    print("TRUE!")
#if-else_elif statements are used to check multiple conditions at once
dogs_age = int(input("How old is your dog in years?"))
if dogs_age < 2:
    print("Your dog is young!")
elif dogs_age > 2 < 7:
    print ("Your dog is an an adult!")
else:
    print("Your dog is old!")
#While loops are used to repeat code for an undertermined number of times
#!= means not equal
first_num = 10
while first_num != 0 :
    print("The number is not zero!")
#these next two line stop the loop
    first_num = first_num -1
    print(first_num)
#a for loop is used to perform the same action
#you determine the number of times it will repeat
first_num = 0
for x in range (5):
    first_num = first_num + x
    print(first_num)
#a function definition is a section of code with a name that can be re-used
def main():
    print("Hello World!")
    
main()
# a parameter is a variable inside a function definition
def Age (age = "20"):
    print ("I am " + age, "years old!")

Age ("17")






