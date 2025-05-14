print("\nWelcome to the Windows Update Tracker v1.1\n")

user_choice = int(input("Press 1 to see the status of all servers\nPress 2 to add a new server.\nPress 3 to update an existing server.\nPress 4 to delete a server\n\n")) 

if user_choice == 1:
    current_patch = str(input("\nWhat is the current security patch KB?\n"))
    print(f"\n Here is the current patch status of all servers\n")
elif user_choice == 2:
    print("\nAdding a new server and it's associated patch\n")
elif user_choice== 3:
    print("\nUpdating an exisiting server and its associated patch\n")
elif user_choice== 4:
    print("\nDeleting an exisiting server and its associated patch\n")    
else:
    print("Your choice is not valid")