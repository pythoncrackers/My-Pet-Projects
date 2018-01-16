subtotal,gratuityrate = eval(input("Enter subtotal and a gratuity rate: "))
gratuity = int((subtotal * (gratuityrate / 100)) * 100) / 100
total = int((subtotal + gratuity) * 100) / 100
print("The gratuity is " + str(gratuity) + " and the total is " + str(total))