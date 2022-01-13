hrs = input("Enter Hours:")
rate = input("Enter rate per Hours:")
hrs_float = float(hrs)
rate_float = float(rate)



if hrs_float <= 40:
    pay = hrs_float * rate_float
    print(pay)
elif hrs_float > 40:
    pay = (40 * rate_float) + ( (hrs_float - 40)* (rate_float * 1.5))
    print(pay)
