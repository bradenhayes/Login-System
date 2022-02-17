import string
import random
import hashlib
from problem2 import addPasswordToDb #This function is imported to be able to use it in this file
'''
isPasswordAcceptable this is a proactive password checker, it checks if the password adheres to the password policy
:param userId: This is the new user Id for the user that is being enrolled
:param userPassword: This is the new user password for the user that is being enrolled
:return "Password accpeted": If the password adheres to the password policy
:return outputtedString: The outputted string that will tell the user all the problems with their password based on the password policy
'''
def isPasswordAcceptable(userId,userPassword):
	counter = 0
	outputtedString = "Errors with your inputted password: \n"
	specialChars = ['!' , '@' , '#' , '$','%' , '?' , '*']
	if (len(userPassword) >=8) and (len(userPassword) <=12):
		counter+=1
	else:
		outputtedString += "Not 8-12 character in length \n"

	if userPassword.islower()!= True:
		counter+=1
	else:
		outputtedString += "Does not contain at least one upper-case letter\n"
	if userPassword.isupper()!=True:
		counter+=1
	else: 
		outputtedString += "Does not contain at least lower-case letter\n"
	for index, char in enumerate(userPassword):
		if char.isdigit():
			counter+=1
			break
		elif index +1==len(userPassword):
			outputtedString+="Does not contain at least one numerical digit\n"
	for index, char in enumerate(userPassword):
		if any(char in specialChars for char in userPassword):
			counter+=1
			break
		elif index +1 ==len(userPassword):
			outputtedString += "Does not contain a special character from the set:{!, @, #, $, %, ?, ∗}\n"
	for index, char in enumerate(userPassword):
		if (not any(char in specialChars for char in userPassword)) and not char.isalpha() and not char.isdigit():
			counter-=1
			outputtedString += "Cannot contain a space or invalid character\n"
			break
	with open('weakPasswords.txt') as f:
		if userPassword in f.read():
			counter-=1
			outputtedString+= "Too similar to commonly used passwords\n"
	if(userPassword!=userId):
		counter+=1
	else:
		outputtedString+="Cannot be the same as user ID\n"

	if counter == 6:
		return "Password accepted"
	else:
		return outputtedString

'''
enrolUser, This function is used to enrol the user into the system, It will call functions to check if the password is acceptable
and then to add the new user to passwd.txt
'''
def enrolUser():
	print("MedView Imaging\nMedical Information Management System \n-------------------------------------------")
	userId = input("Enter new username: ")
	while True:
		userPassword = input("Enter new password: ")
		confirmation = isPasswordAcceptable(userId,userPassword)
		if(confirmation=="Password accepted"):
			print("Password accepted")
			break
		else:
			print(confirmation)
	while True:
		numberInputted = input("Enter the user's role: \nEnter:\n1 for Patient:\n2 for Nurse\n3 For Administrator\n4 for Technical Support\n5 for Physician\n6 for Radiologist\n")
		if numberInputted=="1":
			role="Patient"
			break
		elif numberInputted=="2":
			role="Nurse"
			break
		elif numberInputted=="3":
			role="Administrator"
			break
		elif numberInputted=="4":
			role="Technical Support"
			break
		elif numberInputted=="5":
			role="Physician"
			break
		elif numberInputted=="6":
			role="Radiologist"
			break
		else:
			print("Role does not exist, please only enter 1-6")
	addPasswordToDb(userId,userPassword,role)
	print("User was enrolled successfully")

if __name__ == '__main__':
	enrolUser()