def computepay(h,r):
    if h <= 40 :
        total_pay = (h * r)
    elif h > 40:
        total_pay = (40 * r) + ( (h - 40)* (r * 1.5))
    return total_pay

hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)