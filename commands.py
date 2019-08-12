
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
