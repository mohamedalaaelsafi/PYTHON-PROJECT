from __future__ import barry_as_FLUFL
from multiprocessing.dummy import JoinableQueue
import os
from pickle import TRUE
import re
from tokenize import endpats
import functions as f
import datetime
import fileinput
import sys
from datetime import date

DATE_REG = re.compile(
    r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$')
project = []

def deletecontent():
    open('user_projects', 'w').close()

def check_file_size(filename):
    if os.stat(filename).st_size == 0:
        return False
    else:
        return True


def move_user_projects(email):
    with open('projects') as infile, open('user_projects', 'w') as outfile:
        for line in infile:
            if line.startswith(email):
                outfile.write(line)


def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)


def create_project():
    nv = str(f.newvalue())
    move_user_projects(nv)
    while (TRUE):
        proj_name = input("Enter Project Name: ")
        if not proj_name and not proj_name.isalpha():
            print("Project name cannot be empty.")
        else:
            break
    while (TRUE):
        proj_details = input("Enter Project Details: ")
        if not proj_details:
            print("Project Details cannot be empty.")
        else:
            break
    while (TRUE):
        proj_target = input("Enter project target: ")
        if not proj_target or proj_target.isalpha():
            print("Entry must be integer and not empty.")
        else:
            break
    while (TRUE):
        start_date = input("Enter Start Date in this format yyyy-mm-dd: ")
        end_date = input("Enter End Date in this format yyyy-mm-dd: ")
        if re.fullmatch(DATE_REG, start_date) and re.fullmatch(DATE_REG, end_date):
            break
        else:
            print("Wrong formate.")
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    project.extend((f"{nv}", proj_name, proj_details,
                   proj_target, start_date, end_date, d))
    join_project = " ".join(project)
    print(join_project)
    openfile = open('projects', 'a+')
    openfile.seek(0)
    data = openfile.read(100)
    if len(data) > 0:
        openfile.write("\n")
    openfile.write(join_project)
    openfile.close
    project.clear()
    move_user_projects(nv)


def list_projects():
    if check_file_size("projects") == True:
        with open('projects', "r") as a_file:
            for line in a_file:
                if line[-1] == "\n":
                    print(line[:-1])
                else:
                    print(line)
    else:
        print("No projects found.")


def list_usr_projects():
    nv = str(f.newvalue())
    move_user_projects(nv)
    if check_file_size("user_projects") == True:
        c = 0
        list = []
        with open('user_projects', "r") as a_file:
            for line in a_file:
                if line[-1] == "\n":
                    if line.startswith(f"{nv}"):
                        line = line[:-1].split()
                        c += 1
                        print(c, " ".join(line))
                    else:
                        None
                else:
                    if line.startswith(f"{nv}"):
                        line = line.split()
                        c += 1
                        print(c, " ".join(line))
                    else:
                        None
    else:
        print("No projects found.")


def delete_project():
    testlist = []
    nv = str(f.newvalue())
    move_user_projects(nv)
    list_usr_projects()
    if check_file_size("user_projects") == True:
        while (TRUE):
            try:
                match_number = int(input("Enter book number: "))
                nm = match_number-1
                with open(r"user_projects", 'r+') as fp:
                    lines = fp.readlines()
                    fp.seek(0)
                    fp.truncate()
                    for number, line in enumerate(lines):
                        if number not in [nm]:
                            fp.write(line)

                    testlist.append(lines[nm])
                    joinlist = "".join(testlist)
                    with open(r"projects", "r") as n:
                        lines = n.readlines()
                    with open(r"projects", "w") as n:
                        for line in lines:
                            if line.strip("\n") != joinlist.strip():
                                n.write(line)

                    print(joinlist)
                    print("Deleted.")
                    return
            except:
                print("Wrong entry.")
    else:
        print("No projects found.")


def edit_project():
    if check_file_size("user_projects") == True:
        nv = str(f.newvalue())
        move_user_projects(nv)
        # list_usr_projects()
        num = nv
        c = 0
        mail = []
        name = []
        title = []
        target = []
        startdate = []
        enddate = []
        projectdate = []
        oldrecord = []
        newrecord = []
        with open("user_projects") as search:
            for line in search:
                c += 1
                line = line.rstrip()  # remove '\n' at end of line
                if num in line:
                    print(c, " ", " ".join(line.split()))
                    mail.append(line.split()[0])
                    name.append(line.split()[1])
                    title.append(line.split()[2])
                    target.append(line.split()[3])
                    startdate.append(line.split()[4])
                    enddate.append(line.split()[5])
                    projectdate.append(line.split()[6])
            while (TRUE):
                try:
                    select = int(input("Select Number:"))
                    select = select-1
                    oldrecord.extend((mail[select], name[select], title[select],
                                      target[select], startdate[select], enddate[select], projectdate[select]))
                    new_name = input("Enter new name: ")
                    if not new_name:
                        None
                    else:
                        name[select] = new_name
                    newtitle = input("Enter new title: ")
                    if not newtitle:
                        None
                    else:
                        title[select] = newtitle
                    newtarget = input("Enter new target: ")
                    if not newtarget:
                        None
                    else:
                        target[select] = newtarget
                    newstartdate = input("Enter new start date: : ")
                    if not newstartdate:
                        None
                    else:
                        startdate[select] = newstartdate
                    newenddate = input("Enter new end date: : ")
                    if not newenddate:
                        None
                    else:
                        enddate[select] = newenddate

                    # print(mail[select] , name[select] , title[select], target[select], startdate[select], enddate[select])
                    newrecord.extend((mail[select], name[select], title[select],
                                      target[select], startdate[select], enddate[select], projectdate[select]))
                    joinnewrecord = " ".join(newrecord)
                    joinoldrecord = " ".join(oldrecord)
                    print(f"Old is: {joinoldrecord}")
                    print(f"New is: {joinnewrecord}")

                    replaceAll("user_projects", joinoldrecord, joinnewrecord)
                    replaceAll("projects", joinoldrecord, joinnewrecord)

                    break
                except Exception as e:
                    print("Wrong Entry.")
                    print(e)
    else:
        print("No projects found.")


def searchbydate():
    nv = str(f.newvalue())
    move_user_projects(nv)
    print(nv)
    if check_file_size("user_projects") == True:
        while (TRUE):
            user_date = input("Enter Date in this format yyyy-mm-dd: ")
            print("")
            with open('projects', "r") as file:
                if re.fullmatch(DATE_REG, user_date):
                    try:
                        for line in file:
                            if line.startswith(f"{nv}") and line.strip().endswith(f"{user_date.strip()}"):
                                print(line)

                        break
                    except:
                        print("No Data found.")
                else:
                    print("Wrong formate.")
                break
    else:
        print("No projects found.")


def project_menu():
    nv = str(f.newvalue())
    move_user_projects(nv)
    ans = True
    while ans:
        print("""
        1.Create Project
        2.List your projects
        3.List all projects
        4.Delete your projects
        5.Edit your projets
        6.Search by date
        7.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            create_project()
        elif ans == "2":
            list_usr_projects()
        elif ans == "3":
            list_projects()
        elif ans == "4":
            delete_project()
        elif ans == "5":
            edit_project()
        elif ans == "6":
            searchbydate()
        elif ans == "7":
            print("\n Goodbye")
            exit()
            ans = None
        else:
            print("\n Not Valid Choice Try again")
