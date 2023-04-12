Math = int(input("Enter your maths marks: "))
Eng = int(input("Enter your Eng marks: "))
Hin = int(input("Enter your Hin marks: "))
Sci = int(input("Enter your Sci marks: "))
SST = int(input("Enter your SST marks: "))
Sans = int(input("Enter your Sans marks: "))

percent = ((Math + Eng + Hin + Sci + SST + Sans) / 480) * 100
print(percent)
