weightpounds = eval(input("Enter weight in pounds: "))
heightinches = eval(input("Enter height in inches: "))
weightkgs = weightpounds * 0.45359237
heightmetres = heightinches * 0.0254
bmi = weightkgs / ((heightmetres) ** 2)
print("BMI is ", round(bmi, 4))
