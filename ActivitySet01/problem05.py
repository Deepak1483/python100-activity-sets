# Functions


def computepay(h, r):
    if h>40:
      reg=r*h
      otp=(h-40.0)*(r*0.5)
      p=reg+otp
    else:
      p=h*r
    return p


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
