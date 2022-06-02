year = int(input("Insert year: "))
month = int(input("Insert month (number only): "))
d1 = int(input("Insert Date 1: "))
d2 = int(input("Insert Date 2: "))

date_1 = [year, month, d1]
date_2 = [year, month, d2]

difference_1 = date_1[-1] - date_2[-1]
difference_2 = date_2[-1] - date_1[-1]

if d1 > d2:
  print(f"The difference of {year}-{month}-{d1} and {year}-{month}-{d2} is {difference_1} days.")
else:
  print(f"The difference of {year}-{month}-{d1} and {year}-{month}-{d2} is {difference_2} days.")
