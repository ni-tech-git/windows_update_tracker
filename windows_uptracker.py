import sqlite3

conn = sqlite3.connect('windows_uptracker.db')    #connection object for database. File saved as windows_uptracker.db

cursor = conn.cursor()                                                              #variable called cursor allows for sql commands

cursor.execute("""CREATE TABLE IF NOT EXISTS server_status (          
                server_hostname text,
                operating_system text,
                installed_update text
                  )           
                """)

def add_new_server():
    global new_server
    global new_server_OS
    global new_server_patch
    global new_server_record
                                                              
    new_server = str(input("\nWhat is the name of the new server?\n\n"))
    new_server_OS = str(input("\nWhat OS is it running\n\n"))
    new_server_patch = str(input("\nWhat is its most reason security patch (KB number)\n\n"))

    new_server_record = ({new_server},{new_server_OS},{new_server_patch})

    cursor.execute("INSERT INTO server_status VALUES (?, ?, ?)",(new_server,new_server_OS,new_server_patch))

    conn.commit()

    print(f"The following has been added {new_server_record}")

 

print("\nWelcome to the Windows Update Tracker v1.1\n")

user_choice = int(input("Press 1 to see the status of all servers\nPress 2 to add a new server.\nPress 3 to update an existing server.\nPress 4 to delete a server\n\n")) 


if user_choice == 1:
    print(f"\n Here is the current patch status of all servers\n")
    cursor.execute("SELECT * FROM server_status")
    print(cursor.fetchall())
elif user_choice == 2:
    print("\nAdding a new server and it's associated patch\n")
    add_new_server()
elif user_choice== 3:
    print("\nUpdating an exisiting server and its associated patch\n")
elif user_choice== 4:
    print("\nDeleting an exisiting server and its associated patch\n")    
else:
    print("Your choice is not valid")