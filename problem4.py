import hashlib
from problem1 import accessControl #This function is imported to be able to use it in this file
from problem2 import getDataFromDb #This function is imported to be able to use it in this file
'''
userInterface, This is the main function that is run whenever this file is ran, it will create the basic user interface for
MedView, take a userId and Password in and then call passwordChecker
'''
def userInterface():
	print("MedView Imaging\nMedical Information Management System \n-------------------------------------------");
	while True:
		userId = input("Enter Username: ")
		userPassword = input("Enter password: ")
		result = passwordChecker(userId,userPassword)
		if result=="Access":
			break
		elif result=="Restricted":
			print("Administrators may only access the system during business hours (9AM to 5PM)")
		elif result=="Wrong Password":
			print("Password is incorrect, please try again\n")
		elif result=="Wrong Username":
			print("Username is incorrect, please try again\n")

'''
passwordChecker, This function is used to check if the password and userId combonation exist in the passwd.txt
:param userId: This is the user's id that is passed to get the proper data line from the text file
:param userPassword: This is the user's password that is used to check if the password + the salt equal the hashedpassword
:return permissions: The permissions that the user has
:return "Wrong Username": If the user enter the wrong username
:return "Wrong Password": If the user enters the wrong password
'''
def passwordChecker(userId,userPassword):

	encodedPass = (getDataFromDb(userId,1)+userPassword).encode()
	hashedPassword = hashlib.sha3_512(encodedPass).hexdigest()
	properLogin = getDataFromDb(userId,2)
	if (properLogin == hashedPassword):
		permissions = accessControl(getDataFromDb(userId,3))
		return permissions
	elif properLogin =="No UserId":
		return "Wrong Username"
	else: 
		return "Wrong Password"

if __name__ == "__main__":
    userInterface()