noofminutes = eval(input("Enter the number of minutes: "))
noofdays = noofminutes / 1440
finalnoofyears = int(noofdays // 365)
print("The no of days: " + str(finalnoofyears))
finalnoofdays = int(noofdays % 365)
print("The no of days: " + str(finalnoofdays))
print(str(noofminutes) + " minutes is approximately " + str(finalnoofyears) + " years and " + str(finalnoofdays) + " days ")
