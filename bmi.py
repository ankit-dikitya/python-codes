def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

result = calculate_bmi(weight, height)
print("Your BMI is:", result)

if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result <= 24.9:
    print("You have a normal weight.")
elif 25 <= result <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")