weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

bmi = (weight / (height * height))

if bmi <= 18.5:
    print("Under Weight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Over weight")
else:
    print("Obese")
