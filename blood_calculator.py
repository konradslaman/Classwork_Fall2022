def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - HDL Test")
    print("2 - LDL Test")
    print("9 - Quit")


    keep_Running = True
    while(keep_Running):
        choice = input("Enter choice: ")
        if choice == "9":
            return
        if choice == "1":
            drive_HDL()
        if choice == "2":
            drive_LDL()
        
        

def keyboardInputHDL():
    return int(input("Enter HDL Value: "))
    
def check_HDL(HDL):
    if(HDL>=60):
        return 'Normal'
    elif(HDL>=40):
        return 'Borderline Low'
    else:
        return 'Low'

def output_HDL(val, str):
    print("The results of your HDL test is a value of {} which is {}".format(val,str))


def drive_HDL():
    HDL = keyboardInputHDL()
    level = check_HDL(HDL)
    output_HDL(HDL,level)

def keyboardInputLDL():
    return int(input("Enter LDL Value: "))
    
def check_LDL(LDL):
    if(LDL<130):
        return 'Normal'
    elif(LDL<=159):
        return 'Borderline High'
    elif(LDL<=189):
        return 'High'
    else:
        return 'Very High'

def output_LDL(val, str):
    print("The results of your LDL test is a value of {} which is {}".format(val,str))


def drive_LDL():
    LDL = keyboardInputLDL()
    level = check_LDL(LDL)
    output_LDL(LDL,level)

def keyboardInputTC():
    return int(input("ENter Total Cholesterol Value: "))

def check_TC(TC):
    if(TC<200):
        return 'Normal'
    elif(TC<=239):
        return 'Borderline High'
    else:
        return 'High'

def output_TC(val, str):
    print("The results of your Total Cholesterol test is a value of {} which is {}".format(val,str))

def drive_TC():
    TC = keyboardInputTC()
    level = check_TC(TC)
    output_TC(TC,level)

interface()
