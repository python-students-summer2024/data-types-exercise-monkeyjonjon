"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    projected_total_sales = int(input("What is the projected amount of total sales? "))
    annual_profit = float(projected_total_sales*0.23)
    print(f"Profit: ${annual_profit:,.2f}")


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    dividend = int(input("Please enter a dividend. "))
    divisor = int(input("Please enter a divisor. "))
    quotient = dividend // divisor
    remainder = dividend % divisor
    print (f"{divisor} goes into {dividend} a total of {quotient} times with a remainder of {remainder}")


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = float(input("How many miles has your car driven?"))
    gas_used = float(input("And how many gallons of gas were used?"))
    mpg = (miles_driven/ gas_used)
    print(f"Miles per gallon: {mpg}")

def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1 = float(input("Please enter the first price."))
    price2 = float(input("Please enter the second price."))
    price3 = float(input("Please enter the third price."))
    price1a = format(price1, '.2f')
    price2a = format(price2, '.2f')
    price3a = format(price3, '.2f')
    price1b = str(price1a)
    price2b = str(price2a)
    price3b = str(price3a)
    align1 = format(price1b, '>20s')
    align2 = format(price2b, '>20s')
    align3 = format(price3b, '>20s')
    prices = [(1, align1), (2, align2), (3, align3)]
    print("Here are your prices!", end = "\n\n")
    for n, a in prices:
        print("Price #{n}: ${a}".format(n=n, a=a))