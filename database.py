#database.py
print("This is the database.py module.")
print("Python thinnks this is called {}".format(__name__))

import blood_calculator as bc #This enables us to give the import an alias

#You can also do from blood_calculator import * which does not require the calling of the class before the function
#This solution is bad practice because it can lead to conufion when two imports have a function of the same name

answer = bc.check_HDL(55)
print("The HDL of 55 is {}".format(answer))