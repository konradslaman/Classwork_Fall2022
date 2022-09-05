def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")

    keep_Running = True
    while(keep_Running):
        choice = input("Enter choice: ")
        if choice == "9":
            return
    
    
interface()