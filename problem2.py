import string
import random
import hashlib
'''
addPasswordToDb, This function is used to add a one line entry into the password file record
:param userId: The user's ID to be added to the file
:param userPassword: The user's password to be hashed and added to the file
:param role: The user's role to be added to the file
'''
def addPasswordToDb(userId,userPassword,role):
     salt = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for i in range(32));
     encodedPass = (salt+userPassword).encode()
     hashedPassword = hashlib.sha3_512(encodedPass).hexdigest() 
     f = open("passwd.txt","a")
     f.write(userId+":"+salt+":"+hashedPassword+":"+role+"\n")

'''
getDataFromDb, This function will return data from the database it can return the userId, the salt, the hashed password
or the user's role
:param userId: The user's Id is used to know what line to look on for the salt, hashed password and role
:param index: What index in the row to look at, 0 for userId, 1 for salt, 2 for hashed password and 3 for role
:return individualData[i][index]: Return whatever data is at the index for that corresponding userId
:return "No UserId": If the UserId does not exist in the file then this will be returned
'''
def getDataFromDb(userId,index):
     individualData =[];
     fileObj = open("passwd.txt","r")
     data = fileObj.read().splitlines()
     for i in range(len(data)):
          individualData.append(data[i].split(':'));
     for i in range(len(individualData)):
          if individualData[i][0]==userId:
               if index == 0:
                    return individualData[i][index]
               if index == 1:
                    return individualData[i][index]
               elif index == 2:
                    return individualData[i][index]
               elif index == 3:
                    return individualData[i][index]
     return "No UserId"

