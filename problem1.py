import datetime

#class Employee The basic role that all other employees will inherit(Other than technical support)
class Employee:
    permissions = "View a patient's profile\n"
#class Patient The class for a patient with their permissions
class Patient:
    permissions = "View your patient profile\nView your patient history\nView the contact detail of your Physician"
#class Nurse The class for a nurse that inherits employee's permissions + adds its own
class Nurse:
    permissions = Employee.permissions + "View a patient's history and medical images\n"
#class Radiologist The class for a radiologist that inherits nurse's permissions + adds its own    
class Radiologist:
    permissions = Nurse.permissions +"Suggest a diagnosis\n"
#class Physician The class for a physician that inherits radiologist's permissions + adds its own    
class Physician:
    permissions = Radiologist.permissions + "Prescribe a treatment\n"
#class Administrator The class for an administrator that inherits Employee's permissions + adds its own
class Administrator:
    permissions=Employee.permissions + "Modify a patient's profile\n"
#class TechnicalSupport The class for technical support with its permissions    
class TechnicalSupport:
    permissions= "Run diagnostic tests on imaging units\n"

"""
accessControl, takes the role that a user is assigned and return the permissions that are assigned to that role
:param role: the role that the user is
:return "Access": if the user has an proper role
:return "Restrictied": if the user is an administrator and tries to login outside the hours of 9am-5pm 
""" 
def accessControl(role):
    now=datetime.datetime.now()
    day9am = now.replace(hour=9,minute=0,second=0,microsecond=0)
    day5pm=now.replace(hour=16,minute=0,second=0,microsecond=0)
    if(role!="Administrator"):
        print("User's role: " + role + "\nUser has the following permissions: ")
    if role=="Patient":
        print(Patient.permissions)
        return "Access"
    elif role=="Nurse":
        print(Nurse.permissions)
        return "Access"
    elif role=="Radiologist":
        print(Radiologist.permissions)
        return "Access"
    elif role=="Physician":
        print(Physician.permissions)
        return "Access"
    elif role=="Administrator":
        if now > day9am and now >day5pm:
            return "Restricted"
        else:
            print("User's role: " + role + "\nUser has the following permissions:\n" + Administrator.permissions)
            return "Access"
    elif role=="Technical Support":
        print(TechnicalSupport.permissions)
        return "Access"