# Hi , here is your code for a simple BMI Calculator
# Here h refers to Height and w refers to weight
# bmi = Body Mass Index


# Taking values from user :-
h = float(input("What is your height (In metres):  "))
w = float(input("What is your is weight (In kg): "))

# Calculating BMI:-
bmi = w / (h) ** 2

# Printing statements according to the BMI using If , Elif and Else:-
if bmi <= 18.5:
    print("Your are Malnourished")

elif bmi > 18.5 and bmi <= 24.9:
    print("Your are Healthy")

elif bmi >= 24.9 and bmi < 30:
    print("Your are overweight")

else:
    print("Go do a deit as you Obesed")

print(bmi)
print("Thank you")

# Thank You :)
