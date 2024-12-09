#This code will calculate the BODY MASS INDEX (BMI)

#first we need input like Height and Weight of an individual.
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))

Height = Height/100
#This is the Formula for BMI
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
#Now we will provide the if conditions for various BMI values
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")
