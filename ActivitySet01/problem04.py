# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
if h<40:
 pay=h*10.5
if h>40:
 pay=h*1.5*10.5
print(pay)