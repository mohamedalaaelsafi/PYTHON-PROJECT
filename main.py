from pickle import TRUE
from functions import *

from projects import list_usr_projects, move_user_projects, project_menu

chkfile1 = checkfile("userdata")
checkfile2 = checkfile("projects")
checkfile3 = checkfile("user_projects")
if (chkfile1) == True and (checkfile2) == True and (checkfile3) == True:
    while (TRUE):
        reg_log = input("Enter [l] for login or [r] for register: ")
        if reg_log == "l":
            login()
            break
        elif reg_log == 'r':
            registration()
            print(gl_email)

            project_menu()
            break
        else:
            print("No right entry.")
else:
    print("Error")
