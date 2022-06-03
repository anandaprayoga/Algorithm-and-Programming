num = int(input("Insert number in range 0 to 1000: "))

num_extract1 = num % 10
num_extract2 = num // 10
num_extract3 = num_extract2 // 10
num_extract4 = num_extract2 % 10

sum_num = num_extract1 + num_extract3 + num_extract4
print("The sum of all digit is:", sum_num)
