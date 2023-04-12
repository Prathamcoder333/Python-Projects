# Here is a simple code for making a Unit Converter in Python


# Taking input from User
num = float(input("Tell the no to be converted: "))

# Taking Units from the user to convert
unit1 = str(input("Unit of the number: "))
unit2 = str(input("Unit into which you want to convert: "))

# Length Conversion
if unit1 == "mm" and unit2 == "cm":
    print(num / 10, "cm")

if unit1 == "cm" and unit2 == "m":
    print(num / 100, "m")

if unit1 == "m" and unit2 == "km":
    print(num / 1000, "km")

if unit1 == "cm" and unit2 == "mm":
    print(num * 10, "mm")

if unit1 == "m" and unit2 == "cm":
    print(num * 100, "cm")

if unit1 == "km" and unit2 == "m":
    print(num * 1000, "m")

# Weight Conversion
if unit1 == "mg" and unit2 == "g":
    print(num / 100, "g")

if unit1 == "g" and unit2 == "kg":
    print(num / 1000, "kg")

if unit1 == "g" and unit2 == "mg":
    print(num * 100, "mg")

if unit1 == "kg" and unit2 == "g":
    print(num * 1000, "g")

if unit1 == "kg" and unit2 == "mg":
    print(num * 100000, "mg")

if unit1 == "mg" and unit2 == "g":
    print(num / 100000, "kg")

# Capacity Conversion
if unit1 == "ml" and unit2 == "l":
    print(num / 1000, "l")

if unit1 == "l" and unit2 == "kl":
    print(num / 1000, "kl")

if unit1 == "kl" and unit2 == "l":
    print(num * 1000, "l")

if unit1 == "kl" and unit2 == "ml":
    print(num * 1000000, "ml")

if unit1 == "ml" and unit2 == "kl":
    print(num * 1000000, "kl")

if unit1 == "l" and unit2 == "ml":
    print(num * 1000, "l")

# Thank You :)
