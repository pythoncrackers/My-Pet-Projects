savingamount = eval(input("Enter the monthly saving amount: "))
annualintrate = 0.05
monthlyintrate = annualintrate / 12
value = 1 + monthlyintrate
#After 1 month
value1 = savingamount * value
#After 2 months
value2 = (savingamount + value1) * value
#After 3 months
value3 = (savingamount + value2) * value
#After 4 months
value4 = (savingamount + value3) * value
#After 5 months
value5 = (savingamount + value4) * value
#After 6 months
value6 = (savingamount + value5) * value
print("After the sixth month, the account value is ", round(value6, 2))