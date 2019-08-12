
k_header_magic = "wet"
k_header_version = "0.21"
k_header_code = "test"

import os, sys, shutil, py_compile
from shutil import copyfile
from importlib import reload
# This code by stackoverflow.com, all rights reserved.

class process_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class process:
    def show_start_process(process_name):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Start " + process_name + " process ...")

    def show_fail_process(process_name):
        print("[" + process_colors.FAIL + " Fail " + process_colors.ENDC + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] End " + process_name + " process ...")

    def show_power_on ():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.FAIL + " STOP " + process_colors.ENDC + "] Stop the kernel ...")

    def show_power_off ():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Power off the kernel ...")

    def show_reboot():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Clean switch "+switch+" ...")

    def clean_switch():
        if os.path.isfile ("var/switch_process.pyc"):
            os.remove ("var/switch_process.pyc")
        if os.path.isfile ("etc/switch_user.pyc"):
            os.remove ("etc/switch_user.pyc")

def show_issue():
    issue_filename = "etc/issue"
    file = open (issue_filename,"r")
    strv = file.read()
    file.close()
    print (strv)
def get_hostname():
    hostname_filename = "etc/hostname"
    file = open (hostname_filename,"r")
    strv = file.read()
    file.close()
    return strv


def enter_password(username,command_symbol):
    user_file = "etc/users/"+username
    copyfile (user_file,"etc/switch_user.pyc")
    from etc import switch_user
    switch_user = reload(switch_user)
    i = 1
    while i<6:
        if switch_user.security == True:
            password = input ("Enter "+switch_user.name+"'s password: ")
            if password==switch_user.code:
                k_shell(switch_user.name,command_symbol,"/")
            else:
                print (process_colors.FAIL+"Wrong password.\n"+process_colors.ENDC)
                i = i + 1
        else:
            k_shell(switch_user.name,command_symbol,"/")

def get_permissions (username,permission):
    if username=="root":
        return True
    else:
        if switch_user.admin==True:
            if switch_user.security == True:
                password = input("Enter " + switch_user.name + "'s password: ")
                if password == switch_user.code:
                    return True
                else:
                    print(process_colors.FAIL + "Wrong password.\n" + process_colors.ENDC)
                    return False
            else:
                return True
        else:
            print(process_colors.FAIL +permission+ ": Permission denied." + process_colors.ENDC)
            return False

def shut():
    process.show_end_process("shell")
    process.show_power_off()
    exit(0)
def ver():
    print ("\tKernel name:\t"+process_colors.BOLD+k_header_magic+ " ("+k_header_code+")"+process_colors.ENDC)
    print ("\tKernel type:\t"+process_colors.BOLD+"Hight microkernel"+process_colors.ENDC)
    print ("\tKernel version:\t"+process_colors.BOLD+k_header_version+process_colors.ENDC)

def out(values):
    for i in values:
        print(i.replace("\\n","\n").replace("\\a","\a").replace("\\b","\b").replace("\\f","\f").replace("\\r","\r").replace("\\t","\t").replace("\\v","\v").replace("\\s"," "),end=' ')
def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": file exists." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.WARNING + i + ": directory exists." + process_colors.ENDC)
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": file exists." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.WARNING + i + ": directory exists." + process_colors.ENDC)
            else:
                os.mkdir(root + "/" + i)
def rmdir(values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a directory." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                shutil.rmtree(root + "/" + i, ignore_errors=False, onerror=None)
            else:
                print(process_colors.FAIL + i + ": directory not found." + process_colors.ENDC)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a directory." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                os.rmdir(root + "/" + i)
            else:
                print(process_colors.FAIL + i + ": directory not found." + process_colors.ENDC)

def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
        else:
            print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)
def cat (values):
    if values[0].startswith("-"):
        if values[0].__contains__("b"):
            for i in values[1:]:
                if os.path.isfile(root + "/" + i):
                    file = open(root + "/" + i, "rb")
                    strv = file.read()
                    file.close()
                    print(strv)
                elif os.path.isdir(root + "/" + i):
                    print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
                else:
                    print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
            else:
                print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)

def help():
    print(
        "\t" + process_colors.BOLD + "cat" + process_colors.ENDC + "\t\t[file] ...\tShow files on screen.\n" +
        "\t" + process_colors.BOLD + "cd" + process_colors.ENDC + "\t\t[dir]\t\tChnage directory workspace.\n" +
        "\t" + process_colors.BOLD + "cp" + process_colors.ENDC + "\t\t[src] [dist]\tCopy files.\n" +
        "\t" + process_colors.BOLD + "exit/logout" + process_colors.ENDC + "\t\t\tExit from shell.\n" +
        "\t" + process_colors.BOLD + "ls" + process_colors.ENDC + "\t\t[dir]\t\tList directory.\n" +
        "\t" + process_colors.BOLD + "mkdir" + process_colors.ENDC + "\t\t[dir] ...\tCreate directory.\n" +
        "\t" + process_colors.BOLD + "mv" + process_colors.ENDC + "\t\t[src] [dist]\tMove or rename files.\n" +
        "\t" + process_colors.BOLD + "out" + process_colors.ENDC + "\t\t[...]\t\tPrint message on screen.\n" +
        "\t" + process_colors.BOLD + "passwd" + process_colors.ENDC + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.BOLD + "pyc" + process_colors.ENDC + "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.BOLD + "reboot" + process_colors.ENDC + "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.BOLD + "rm" + process_colors.ENDC + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.BOLD + "rmdir" + process_colors.ENDC + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.BOLD + "shut" + process_colors.ENDC + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.BOLD + "su" + process_colors.ENDC + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.BOLD + "useradd" + process_colors.ENDC + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.BOLD + "userinfo" + process_colors.ENDC + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.BOLD + "userlist" + process_colors.ENDC + "\t\t\tList users account.\n" +
        "\t" + process_colors.BOLD + "userm" + process_colors.ENDC + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.BOLD + "ver" + process_colors.ENDC + "\t\t\t\tShow informations about kernel."
    )
def cp (values):
    if values[0].startswith("-"):
        if values[0].__contains__("r"):
            if os.path.isdir(root + "/" + values[1]):
                if os.path.isfile(root + "/" + values[2]):
                    print(process_colors.FAIL + values[2] + ": dest isn't a directory." + process_colors.ENDC)
                else:
                    shutil.copytree(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isfile(root + "/" + values[1]):
                print(process_colors.FAIL + values[1] + ": source isn't a directory." + process_colors.ENDC)
            else:
                print(process_colors.FAIL + values[1] + ": source not found." + process_colors.ENDC)
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/" + values[1]):
                print(process_colors.FAIL + values[1] + ": dest isn't a file." + process_colors.ENDC)
            else:
                shutil.copyfile(root + "/" + values[0], root + "/" + values[1])
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.FAIL + values[0] + ": source isn't a file." + process_colors.ENDC)
        else:
            print(process_colors.FAIL + values[0] + ": source not found." + process_colors.ENDC)
def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+dest)
    else:
        print(process_colors.FAIL + values[0] + ": source not found." + process_colors.ENDC)
def useradd (username):
    if not (os.path.isdir("desk/"+username) or os.path.isfile("etc/users/"+username)):
        admin = input("Choose user type [A/S]: ")
        if admin=="A" or admin=="a":
            file = open("etc/users/" + username + ".py", "w")
            file.write("admin = True\n")
            file.close()
        elif admin=="S" or admin=="s":
            file = open("etc/users/" + username + ".py", "w")
            file.write("admin = False\n")
            file.close()
        security = input("Choose user security [T/f]: ")
        file = open("etc/users/" + username + ".py", "a")
        file.write("name = \"" + username + "\"\n")
        if security=="T" or security=="t":
            while True:
                password = input ("Set user a new password: ")
                code = input ("Confirm a new password: ")
                if password==code:
                    file.write("security = True\n")
                    file.write("code = \"" + password + "\"")
                    file.close()
                    break
                else:
                    print(process_colors.FAIL + "Wrong password! Try agian.\n" + process_colors.ENDC)
        elif security=="f" or security=="F" or security=="\0":
            file.write("security = False\n")
            file.close()
        correct = input ("Is this information correct? [Y/n]: ")
        if correct=="n" or correct=="N" or correct=="\0":
            file.close()
            os.remove ("etc/users/"+username+".py")
        elif correct=="Y" or correct=="y":
            file.close()
            src = "etc/users/"+username+".py"
            dest = "etc/users/"+username
            py_compile.compile(src,dest)
            os.remove(src)
            os.mkdir ("desk/"+username)
    else:
        print(process_colors.FAIL + username + ": user already exists." + process_colors.ENDC)
def userm (username):
    if username=="root":
        print(process_colors.FAIL +username+ ": cannot remove root user account: Is a permanent user." + process_colors.ENDC)
    elif os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
        keep = input ("Are you going to keep this " + username+"'s files? [Y/n]: ")
        if keep=="Y" or keep=="y":
            os.remove("etc/users/"+username)
        elif keep=="N" or keep=="n" or keep=="\0":
            shutil.rmtree("desk/"+username,ignore_errors=False, onerror=None)
            os.remove("etc/users/"+username)
    else:
        print(process_colors.FAIL +username+ ": user not found." + process_colors.ENDC)
def passwd (username):
    if username=="root" and os.path.isdir("root") and os.path.isfile("etc/users/root"):
        shutil.copyfile("etc/users/" + username, "etc/switch_user.pyc")
        from etc import switch_user
        switch_user = reload(switch_user)
        if switch_user.security == True:
            login = input("Enter " + username + "'s password: ")
            if login == switch_user.code:
                change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                if change_security == "Y" or change_security == "y":
                    security = input("Change user security [T/f]: ")
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("name = \"" + username + "\"\n")
                    if security == "T" or security == "t":
                        change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                        if change_password == "Y" or change_password == "y":
                            while True:
                                password = input("Set user a new password: ")
                                code = input("Confirm a new password: ")
                                if password == code:
                                    file.write("security = True\n")
                                    file.write("code = \"" + password + "\"")
                                    file.close()
                                    break
                                else:
                                    print(
                                        process_colors.FAIL + "Wrong password! Try agian.\n" + process_colors.ENDC)
                        elif change_password == "n" or change_password == "N":
                            file.write("security = True\n")
                            file.write("code = \"" + switch_user.code + "\"")
                            file.close()
                    elif security == "f" or security == "F" or security == "\0":
                        file.write("security = False\n")
                        file.close()
                elif change_security == "n" or change_security == "N" or  change_security == "\0":
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("security = " + str(switch_user.security) + "\n")
                    file.close()
            else:
                print(process_colors.FAIL + "Wrong password." + process_colors.ENDC)
        else:
            change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
            if change_security == "Y" or change_security == "y":
                security = input("Change user security [T/f]: ")
                file = open("etc/users/" + username + ".py", "a")
                file.write("name = \"" + username + "\"\n")
                if security == "T" or security == "t":
                    change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                    if change_password == "Y" or change_password == "y":
                        while True:
                            password = input("Set user a new password: ")
                            code = input("Confirm a new password: ")
                            if password == code:
                                file.write("security = True\n")
                                file.write("code = \"" + password + "\"")
                                file.close()
                                break
                            else:
                                print(process_colors.FAIL + "Wrong password! Try agian.\n" + process_colors.ENDC)
                    elif change_password == "n" or change_password == "N" or change_password == "\0":
                        file.write("security = True\n")
                        file.write("code = \"" + switch_user.code + "\"")
                        file.close()
                elif security == "f" or security == "F" or  security == "\0":
                    file.write("security = False\n")
                    file.close()
            elif change_security == "n" or  change_security == "N" or  change_security == "\0":
                file = open("etc/users/" + username + ".py", "a")
                file.write("security = " + str(switch_user.security) + "\n")
                file.close()

        src = "etc/users/" + username + ".py"
        dest = "etc/users/" + username
        if os.path.isfile(src):
            py_compile.compile(src, dest)
            os.remove(src)
    else:
        if os.path.isfile("etc/users/" + username) and os.path.isdir("desk/" + username):
            shutil.copyfile("etc/users/" + username, "etc/switch_user.pyc")
            from etc import switch_user
            if switch_user.security == True:
                login = input("Enter " + username + "'s password: ")
                if login == switch_user.code:
                    change_admin = input("Do you want to change " + username + "'s type? [Y/n]: ")
                    if change_admin == "Y" or change_admin == "y":
                        admin = input("Change user type [A/S]: ")
                        if admin == "A" or admin == "a":
                            file = open("etc/users/" + username + ".py", "w")
                            file.write("admin = True\n")
                            file.close()
                        elif admin == "S" or admin == "s":
                            file = open("etc/users/" + username + ".py", "w")
                            file.write("admin = False\n")
                            file.close()
                    elif change_admin == "n" or change_admin == "N" or change_admin == "\0":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = " + str(switch_user.admin) + "\n")
                        file.close()
                    change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                    if change_security == "Y" or change_security == "y":
                        security = input("Change user security [T/f]: ")
                        file = open("etc/users/" + username + ".py", "a")
                        file.write("name = \"" + username + "\"\n")
                        if security == "T" or security == "t":
                            change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                            if change_password == "Y" or change_password == "y":
                                while True:
                                    password = input("Set user a new password: ")
                                    code = input("Confirm a new password: ")
                                    if password == code:
                                        file.write("security = True\n")
                                        file.write("code = \"" + password + "\"")
                                        file.close()
                                        break
                                    else:
                                        print(
                                            process_colors.FAIL + "Wrong password! Try agian.\n" + process_colors.ENDC)
                            elif change_password == "n" or change_password == "N" or change_password == "\0":
                                file.write("security = True\n")
                                file.write("code = \"" + switch_user.code + "\"")
                                file.close()
                        elif security == "f" or security == "F" or security == "\0":
                            file.write("security = False\n")
                            file.close()
                    elif change_security == "n" or change_security == "N" or change_security == "\0":
                        file = open("etc/users/" + username + ".py", "a")
                        file.write("security = " + str(switch_user.security) + "\n")
                        file.close()
                else:
                    print(process_colors.FAIL + "Wrong password." + process_colors.ENDC)
            else:
                change_admin = input("Do you want to change " + username + "'s type? [Y/n]: ")
                if change_admin == "Y" or change_admin == "y":
                    admin = input("Change user type [A/S]: ")
                    if admin == "A" or  admin == "a":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = True\n")
                        file.close()
                    elif admin == "S" or admin == "s":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = False\n")
                        file.close()
                elif change_admin == "n" or change_admin == "N" or change_admin == "\0":
                    file = open("etc/users/" + username + ".py", "w")
                    file.write("admin = " + str(switch_user.admin) + "\n")
                    file.close()
                change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                if change_security == "Y" or change_security == "y":
                    security = input("Change user security [T/f]: ")
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("name = \"" + username + "\"\n")
                    if security == "T" or security == "t":
                        chnage_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                        if chnage_password == "Y" or chnage_password == "y":
                            while True:
                                password = input("Set user a new password: ")
                                code = input("Confirm a new password: ")
                                if password == code:
                                    file.write("security = True\n")
                                    file.write("code = \"" + password + "\"")
                                    file.close()
                                    break
                                else:
                                    print(process_colors.FAIL + "Wrong password! Try agian.\n" + process_colors.ENDC)
                        elif chnage_password == "n" or chnage_password == "N" or chnage_password == "\0":
                            file.write("security = True\n")
                            file.write("code = \"" + switch_user.code + "\"")
                            file.close()
                    elif security == "f" or security == "F" or security == "\0":
                        file.write("security = False\n")
                        file.close()
                elif change_security == "n" or change_security == "N" or change_security == "\0":
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("security = " + str(switch_user.security) + "\n")
                    file.close()

            src = "etc/users/" + username + ".py"
            dest = "etc/users/" + username
            if os.path.isfile(src):
                py_compile.compile(src, dest)
                os.remove(src)
        else:
            print(process_colors.FAIL + username + ": user not found." + process_colors.ENDC)
def userinfo (username):
    if username=="root" and os.path.isdir ("root") and os.path.isfile ("etc/users/root"):
        copyfile("etc/users/" + username, "etc/switch_user.pyc")
        from etc import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.BOLD + switch_user.name + process_colors.ENDC)
        if switch_user.security == True:
            print("    Security:   " + process_colors.BOLD + "enable" + process_colors.ENDC)
        else:
            print("    Security:   " + process_colors.BOLD + "disable" + process_colors.ENDC)
    elif os.path.isdir ("desk/"+username) and os.path.isfile("etc/users/"+username):
        copyfile("etc/users/" + username, "etc/switch_user.pyc")
        from etc import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.BOLD + switch_user.name + process_colors.ENDC)
        if switch_user.admin == True:
            print("    Type:       " + process_colors.BOLD + "Administrator" + process_colors.ENDC)
        else:
            print("    Type:       " + process_colors.BOLD + "Standard" + process_colors.ENDC)
        if switch_user.security == True:
            print("    Security:   " + process_colors.BOLD + "enable" + process_colors.ENDC)
        else:
            print("    Security:   " + process_colors.BOLD + "disable" + process_colors.ENDC)
    elif username=="" or username==" ":
        print()
    else:
        print(process_colors.FAIL +username+ ": user not found." + process_colors.ENDC)
def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.ENDC)
            else:
                print(process_colors.BOLD + process_colors.OKBLUE + dir + "/" + process_colors.ENDC)
    else:
        print(process_colors.FAIL +path+ ": directory not found." + process_colors.ENDC)
def pyc (values):
    if values[0].startswith("-"):
        if values[0].__contains__("o"):
            if os.path.isfile(root + "/" + values[1]):
                if os.path.isdir(root + "/" + values[2]):
                    print(process_colors.FAIL + values[2] + ": source isn't a file." + process_colors.ENDC)
                else:
                    py_compile.compile(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isdir(root + "/" + values[1]):
                print(process_colors.FAIL + values[1] + ": source isn't a file." + process_colors.ENDC)
            else:
                print(process_colors.FAIL + values[1] + ": source not found." + process_colors.ENDC)
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/"+str(values[0].replace(".py",""))+".pyc"):
                print(process_colors.FAIL + str(values[0].replace(".py",""))+".pyc" + ": dest isn't a file." + process_colors.ENDC)
            else:
                py_compile.compile(root + "/" + values[0], root + "/" + str(values[0].replace(".py",""))+".pyc")
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.FAIL + values[0] + ": source isn't a file.." + process_colors.ENDC)
        else:
            print(process_colors.FAIL + values[0] + ": source not found." + process_colors.ENDC)
def exec (filename,args):
    if os.path.isfile(root + "/bin/" + filename + ".pyc"):
        process.clean_switch()
        copyfile(root + "/bin/"+ filename + ".pyc", "var/switch_process.pyc")
        from var import switch_process
        switch_process = reload(switch_process)
        switch_process.main(args)
        process.clean_switch()
def su (user_already,username):
    if user_already==username:
        print(process_colors.WARNING +username+ ": user already switched." + process_colors.ENDC)
    else:
        if username=="root":
            enter_password("root","#")
        elif os.path.isdir ("desk/"+username) and os.path.isfile ("etc/users/"+username):
            enter_password(username,"$")
        else:
            print(process_colors.FAIL + username + ": user not found." + process_colors.ENDC)
def logout():
    k_clean()
    k_login()
def reboot():
    k_clean()
    import vmwet
    vmwet = reload(vmwet)
def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.BOLD+"    "+user+process_colors.ENDC+"\tActive")
        else:
            print (process_colors.BOLD+process_colors.FAIL+"    "+user+process_colors.ENDC+"    Inactive")
    print(process_colors.BOLD + "    root"+process_colors.ENDC + "\tActive")

root = "."
path = "/"

def k_init():
    process.show_power_on()
    process.show_start_process("init")

k_init()
def k_clean():
    process.show_start_process("clean")
    process.show_clean_switch("process")
    process.show_clean_switch("user")
    process.clean_switch()

def k_distro ():
    process.show_start_process("distro")

    from etc import distro

    print("\n"+"Welcome to "+distro.name+" "+distro.version+"\n")

k_distro()

def k_issue():
    process.show_start_process("issue")

    print()
    show_issue()
    print()

k_issue()
def terminal(commandline,command,username,command_symbol,path):
    if command == "" or command == " " or command.startswith("#") or command.startswith("//") or (command.startswith("/*") and command.endswith("*/")):
        print(end='')
    elif command == "shut":
        print()
        shut()
    elif command == "ver":
        ver()
    elif commandline[0] == "out":
        out(commandline[1:])
    elif commandline[0] == "mkdir":
        mkdir(commandline[1:])
    elif commandline[0] == "rmdir":
        rmdir(commandline[1:])
    elif commandline[0] == "rm":
        rm(commandline[1:])
    elif commandline[0] == "cat":
        cat(commandline[1:])
    elif command == "help":
        help()
    elif commandline[0] == "cp":
        cp(commandline[1:])
    elif commandline[0] == "mv":
        mv(commandline[1:])
    elif commandline[0] == "useradd":
        useradd(commandline[1])
    elif commandline[0] == "userm":
        userm(commandline[1])
    elif commandline[0] == "passwd":
        passwd(commandline[1])
    elif command == "userinfo":
        userinfo(username)
    elif commandline[0] == "userinfo":
        userinfo(commandline[1])
    elif command == "ls":
        ls(path)
    elif commandline[0] == "ls":
        ls(commandline[1])
    elif commandline[0] == "su":
        su(username, commandline[1])
    elif command == "logout" or command == "exit":
        print()
        process.show_end_process("shell")
        logout()
    elif command == "reboot":
        print()
        process.show_end_process("shell")
        process.show_reboot()
        reboot()
    elif commandline[0] == "pyc":
        pyc(commandline[1:])
    elif command == "userlist":
        userlist()
    elif os.path.isfile("bin/" + commandline[0] + ".pyc"):
        exec(commandline[0], commandline[1:])
    else:
        print(process_colors.FAIL + commandline[0] + ": command not found." + process_colors.ENDC)

def k_shell(username,command_symbol,path):
    print()
    process.show_start_process("shell")
    print()
    while True:
        color_prompt = process_colors.ENDC
        color_path = process_colors.ENDC
        if username=="root":
            color_prompt = process_colors.ENDC
            color_path = process_colors.ENDC
        else:
            color_prompt = process_colors.OKGREEN
            color_path = process_colors.OKBLUE

        command = input (process_colors.BOLD+color_prompt+username+"@"+get_hostname()+process_colors.ENDC+":"+color_path+path+process_colors.ENDC+ command_symbol+" ")
        commandline = command.split(" ")

        if commandline[0] == "cd":
            for i in commandline[1:]:
                if commandline[1]=="" or commandline[1]==" ":
                    path = ""
                elif commandline[1].startswith("/"):
                    if os.path.isdir(root + "/" + commandline[1]):
                        path = commandline[1]
                    else:
                        print(process_colors.FAIL + commandline[1] + ": directory not found." + process_colors.ENDC)
                else:
                    if os.path.isdir(root+"/"+path+"/"+commandline[1]):
                        if path == "/":
                            path = path + commandline[1]
                        else:
                            path = path + "/" + commandline[1]
                    else:
                        print(process_colors.FAIL + commandline[1] + ": directory not found." + process_colors.ENDC)
        else:
            terminal(commandline,command,username,command_symbol,path)

def k_login():
    process.show_start_process("login")

    while True:
        username = input ("\nEnter a username: ")
        if username=="root" and os.path.isdir ("root") and  os.path.isfile("etc/users/root"):
            enter_password("root","#")
        if os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
            enter_password(username,"$")
        elif username=="" or username.startswith(" "):
            continue
        else:
            print (process_colors.FAIL+username+": user not found."+process_colors.ENDC)

k_login()
