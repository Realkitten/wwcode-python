""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

# Build your code below
bill =int(input ('how much is your bill?'))
payment =int (input ('how much is your payment?'))
a = bill - payment
print ('hi! your change is ' ,+a)