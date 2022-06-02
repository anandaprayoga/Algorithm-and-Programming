filename = str(input("Insert filename with extension (ex: Test.txt): "))
output = filename.split(".")
print("Your extension is: " + output[-1])
