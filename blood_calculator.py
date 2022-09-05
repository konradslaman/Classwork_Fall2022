def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")

    keep_Running = True
    while(keep_Running):
        choice = input("Enter choice: ")
        if choice == "9":
            return

def keyboardInputHDL():
    return int(input("Enter HDL Value:"))
    
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

interface()
