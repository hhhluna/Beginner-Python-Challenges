
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
bmi1= round(bmi)
bmi2=str(bmi1)
if bmi< 18.5:
    print("Your BMI is "+ bmi2+", you are underweight.");
elif bmi < 25:
    print("Your BMI is "+ bmi2+", you have a normal weight.");
elif bmi < 30:
    print("Your BMI is "+ bmi2+", you are slightly overweight.");
elif bmi < 35:
    print("Your BMI is "+ bmi2+", you obese.");
else:
    print("Your BMI is "+ bmi2+", you are clinically obese.");
