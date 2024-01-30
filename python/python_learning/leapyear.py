year=int(input("Enter the year : "))
if year%400==0 or year%100!=0 and year%4==0:
    print("the given year {} is leapyear".format(year))
else:
    print("the given year {} is Not a leapyear".format(year))