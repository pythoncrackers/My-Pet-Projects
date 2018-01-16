x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
side1 = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
#print("the side1 is : " + str(side1))
####
side2 = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** 0.5
#print("the side2 is : " + str(side2))
####
side3 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
#print("the side3 is : " + str(side3))

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
area = int((area * 10)) / 10
print("The area of the triangle is: " + str(area))