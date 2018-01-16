number = eval(input("Enter a number between 0 and 1000: "))
unitdigit = number % 10
print("The units digit is: " + str(unitdigit))
tensdigit = (number // 10) % 10
print("The tens digit is: " + str(tensdigit))
hundredsdigit = (number // 10) // 10
print("The hundreds digit is: " + str(hundredsdigit))

sum = unitdigit + tensdigit + hundredsdigit
print("The sum of the digits is " + str(sum))
