from pickle import TRUE
# import projects as p
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
usr_reg = []
gl_email = ""


def checkfile(filename):
    userdata = open(filename, 'a+')
    userdata.close
    return True


def checkprojects():
    userdata = open('projects', 'a+')
    userdata.close
    return True


def password():
    while (TRUE):
        passwd = input("Enter a password: ")
        if len(passwd) < 6:
            print("Password must be equal to 6 or more characters.")
        else:
            usr_reg.append(passwd)
            break
    while (TRUE):
        conf_passwd = input("Confirm password: ")
        if conf_passwd == passwd:
            break
        else:
            print("Password not match.")


def registration():
    import projects as p
    while (TRUE):
        fname = input("Enter your first name: ")
        if not fname or not fname.isalpha():
            print("Not valid name.")
            continue
        else:
            usr_reg.append(fname)
            break
    while (TRUE):
        lname = input("Enter your Last name: ")
        if not lname or not lname.isalpha():
            print("Not valid name.")
        else:
            usr_reg.append(lname)
            break
    while (TRUE):
        email = input("Enter your email: ")
        if (re.fullmatch(regex, email)):
            #    usr_reg.append(email)
            f = open("userdata", "r")
            lines = f.readlines()
            result = []
            for x in lines:
                result.append(x.split(' ')[1])
            f.close()
            result = [x.split(' ')[2] for x in open("userdata").readlines()]
            try:
                result.index(email)
                print("Email is already exists.")
            except:
                usr_reg.append(email)
                break
        else:
            print("Not Valid email.")
    password()
    while (True):
        phone_number = input("Enter your number: ")
        if phone_number.isnumeric() and phone_number.startswith("01") and len(phone_number) == 11:
            usr_reg.append(phone_number)
            break
        else:
            print("Not valid number")
    joindata = " ".join(usr_reg)
    openfile = open('userdata', 'a+')
    openfile.seek(0)
    data = openfile.read(100)
    if len(data) > 0:
        openfile.write("\n")
    openfile.write(joindata)
    openfile.close
    global gl_email
    gl_email = email
    print(gl_email)


def find_row(email):

    c = 0
    with open('userdata', "r") as a_file:
        for line in a_file:
            c += 1
            if email in line:
                return line


def login():
    import projects as p
    while (TRUE):
        email = input("Enter your email: ")
        f = open("userdata", "r")
        lines = f.readlines()
        result = []
        for x in lines:
            result.append(x.split(' ')[1])
        f.close()
        result = [x.split(' ')[2] for x in open("userdata").readlines()]
        try:
            result.index(email)
            fw = find_row(email).split(" ")
            match_email = fw[2]
            if fw[3][-1] == "\n":
                match_password = fw[3][:-1]
            else:
                match_password = fw[3]
            # print(c)
            break
        except:
            print("Email not found.")

    while (TRUE):
        passwd = input("Enter your password: ")
        if passwd == match_password:
            break
        else:
            print("Password not matched.")
    global gl_email
    gl_email = email
    p.project_menu()


def newvalue():
    return str(gl_email)


print(newvalue())
