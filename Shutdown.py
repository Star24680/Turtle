Question = input("Do you want to shut down the system? (Yes/No): ")

if Question == "Yes":
    Work = input("Do you want to save unsaved work? (Yes/No): ")
    
    if Work == "Yes":
        print("Saving work and shutting down...")
    elif Work == "No":
        print("Shutting down without saving...")
    else:
        print("Sorry, invalid input for saving work.")
    
elif Question == "No":
    print("Abort shut down.")
    
else:
    print("Sorry, invalid input.")
