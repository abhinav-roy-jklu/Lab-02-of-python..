#LAB2
#Q1

'''
n=int(input("Enter a number:"))
if n%5==0:
    print("Hi")
else:
    print("Bye")

#Q2
x=float(input("Enter first parallel side:"))
y=float(input("Enter second parallel side:"))
h=float(input("Enter height:"))
area=(x+y)*h/2
print("Area of trapezoid:",area)

#Q3
w=float(input("Enter weight in kg:"))
h=float(input("Enter height in m:"))
bmi=w/(h*h)
print("BMI:",round(bmi,2))
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal weight")
elif bmi<30:
    print("Slightly overweight")
elif bmi<35:
    print("Obese")
else:
    print("Clinically obese")

#Q4
ch=input("Enter an alphabet:").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#Q5
old=2.19e14
new=4.68e14
growth=(new-old)/old*100
print("Bacterial growth:",round(growth),"%")

#Q6
m=int(input("Enter number of months:"))
y=m//12
r=m%12
print("Years:",y)
print("Months:",r)

#Q7
color=input("Enter color (Blue/Red):").lower()
mode=input("Enter mode (Steady/Flashing):").lower()
if color=="blue" and mode=="steady":
    print("Clear view")
elif color=="blue" and mode=="flashing":
    print("Clouds due")
elif color=="red" and mode=="steady":
    print("Rain ahead")
elif color=="red" and mode=="flashing":
    print("Snow instead")
else:
    print("Invalid input")

#Q8
cost=float(input("Enter total costs:"))
rev=float(input("Enter total revenue:"))
if cost==rev:
    print("Break even")
elif rev>cost:
    print("Profit:",rev-cost)
else:
    print("Loss:",cost-rev)

#Q9
n=int(input("Enter number of widgets:"))
if n>=100:
    total=n*0.20
else:
    total=n*0.25
print("Total cost: $",round(total,2))

#Q10
p=float(input("Enter pounds of apples:"))
cash=float(input("Enter cash tendered:"))
cost=p*2.50
change=cash-cost
if change>=0:
    print("Change: $",round(change,2))
else:
    print("You owe $"+format(-change,".2f")+" more.")

#Q11
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
if a>=b:
    if a>=c:
        largest=a
    else:
        largest=c
else:
    if b>=c:
        largest=b
    else:
        largest=c
print("Largest number:",largest)

#Q12
basic=float(input("Enter basic salary:"))
hra=basic*0.20
ta=basic*0.05
da=basic*0.10
gross=basic+hra+ta+da
print("Gross salary:",gross)

#Q13
basic=float(input("Enter basic salary:"))
gross=basic+(basic*0.20)+(basic*0.05)+(basic*0.10)
print("Gross salary:",gross)
if gross<300000:
    tax=0
elif gross<=1000000:
    tax=gross*0.10
elif gross<=2500000:
    tax=gross*0.20
else:
    tax=gross*0.30
print("Income tax:",tax)
print("Salary after tax:",gross-tax)

#Q14
income=float(input("Enter taxable income:"))
if income<=20000:
    tax=income*0.02
elif income<=50000:
    tax=400+0.025*(income-20000)
else:
    tax=1150+0.035*(income-50000)
print("State income tax:",round(tax,2))