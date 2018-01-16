#5
'''
subtotal = eval(input("Enter subtotal:"))
gratuity = eval(input("Enter gratuity in %:"))
g = (gratuity/100*subtotal)
print("The gratuity is : "+ str(round(g,2)) + " and total is: " + str(round((subtotal + g),2))
'''
#6
'''
number = eval(input("Enter a number between 0 and 1000:"))
print("The sum of the digits is: " + str((number//100)+((number%100)//10)+(((number%10)%10))))
'''
#7
'''
minutes = eval(input("ENter number of minutes:"))
print(str(minutes) +" minutes is approximately :"+ str(minutes//(60*24*365)) + " years " + str(round((minutes/(60*24*365)-(minutes//(60*24*365)))*365)) + " days")
'''
#14
'''
x1=eval(input("Input x1"))
y1 = eval(input("Input y1"))
x2=eval(input("Input x2"))
y2 = eval(input("Input y2"))
x3=eval(input("Input x3"))
y3 = eval(input("Input y3"))
sd1 = (x2-x1)**(2) + (y2-y1)**(2)
sd1 = sd1**(1/2)
sd2 = (x2-x3)**(2) + (y2-y3)**(2)
sd2 = sd2**(1/2)
sd3 = (x3-x1)**(2) + (y3-y1)**(2)
sd3 = sd3**(1/2)
s = (sd1+sd2+sd3)/2
area=s*(s-sd1)*(s-sd2)*(s-sd3)
area = area**(1/2)
print("The area of the triangle:" + str(round(area,2)))
'''
#17
'''
weight = eval(input("Enter weight in pounds: "))
height = eval (input("Enter height in inches: "))
weight = weight * 0.45359237
height = height* 0.0254
bm1 = weight/((height)**(2))
print("BMI is :" + str(round(bm1,4)))
'''
#21
'''
saving = eval(input("Enter the monthly saving amount:"))
saving_sum = saving*(1+5/(100*12))
for i in range(0,5):
    saving_sum = (saving + saving_sum)*(1+5/(100*12))
print("After the sixth month, the account value :"+ str(round(saving_sum,2)))
'''
#25
import turtle

x = eval(input("Input centre x coordinate of rectangle:"))
y = eval(input("Input centre y coordinate of rectangle:"))
width = eval(input("Input width:"))
height = eval(input("Input height:"))
turtle.penup()

turtle.goto(x,y)
turtle.right(90)
turtle.forward(width/2)
turtle.left(90)
turtle.pendown()
turtle.forward(height/2)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height/2)





turtle.done()




