#######################################################################################################################################################
# 
# Name: Rupak Santra
# SID: 740093310
# Exam Date: 27th March 2024
# Module: BEMM458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-RS07UEBS
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# Initialize an empty list to store (start, end) positions
my_list = []
#looping through each value in key comments 
for key, value in key_comments.items():
    #finding the start and end position of each value in the customer feedback
    #appending the start and end position of each value in the list my_list
    my_list.append(((customer_feedback.find(value)), customer_feedback.find(value)+len(value)))

print(my_list)
#output : [(38, 50), (12, 17), (114, 120), (88, 94), (142, 150), (99, 109), (18, 28), (129, 136), (51, 58), (82, 87)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
x = 74
# Insert last two digits of ID number here:10
y = 10

# Write your code for Operating Profit Margin
def operating_profit_margin(revenue, net_profit):
    #calculating profit margin by dividing net profit by revenue and multiplying by 100 to get percentage
    profit_margin = (net_profit/revenue)*100
    return profit_margin

# Write your code for Revenue per Customer
def revenue_per_customer(revenue, customers):
    #calculating revenue per customer by dividing revenue by number of customers
    revenue_per_customer = revenue/customers
    return revenue_per_customer

# Write your code for Customer Churn Rate
def customer_churn_rate(customers_beginning, customers_end):
    #calculating churn rate by subtracting number of customers at the end of the period from number of customers at the beginning of the period
    churn_rate = ((customers_beginning - customers_end)/customers_beginning)*100
    return churn_rate

# Write your code for Average Order Value
def average_order_value(revenue, orders):
    average_order_value = revenue/orders
    return average_order_value

# Call your designed functions here
print("Opertating Profit Margin:" ,operating_profit_margin(x, y))
#output : Opertating Profit Margin: 13.513513513513514
# This means the company generate 13.51p profit for every £1 of revenue after covering all expenses.
print("Revenue Per Customer:" ,revenue_per_customer(x, y))
#output : Revenue Per Customer: 7.4
# This means the company generated £7.4 revenue per customer
print("Customer Churn Rate:", customer_churn_rate(x, y))
#output : Customer Churn Rate: 86.48648648648648
# This means the company lost 86.48% of its customers during the period.
print("Average Order Value:",average_order_value(x, y))
#output : Average Order Value: 7.4
# This means the average order value of every order is £7.4

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Creating array with the given dataset
Price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
Demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Linear Regression Model
model = LinearRegression()
model.fit(Price, Demand)

# Predicting demand when product price is £52
price_demand = np.array([[52]])
predicted_demand = model.predict(price_demand)
print("Predicted Demand when price is £52 is" ,predicted_demand[0], "units")

# Plotting
plt.scatter(Price, Demand, color='blue', label='Data Points')
plt.plot(Price, model.predict(Price), color='darkgreen', label='Regression Line')

# Add labels and title
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs. Demand')
plt.legend()
plt.show()

#Output : Predicted Demand when price is £52 is 158.17272727272726 units
#Comment : As per the linear regression model, the demand is highest when the price is £45.


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random numbers between 1 and student id number
#"-" can not contains in varialbe name, so chnaged it to "_"
#input function is not defined, so changed it with import numpy as np and then we need to use np.int64
max_value = np.int64(input("Enter your Student ID: "))

random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
#markercolor should be markerfacecolor and markeredgcolor should be markeredgecolor and lable should be label and 'O' should be 'o'
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue');
#title should be in quotes, so added quotes
plt.title('Line Chart of 100 Random Numbers')
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
plt.grid(True)
plt.show()



