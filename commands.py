
def shut():
    process.show_end_process("shell")
    process.show_power_off()
    exit(0)
def ver():
    py_compile.compile("etc/distro", "var/distro.pyc")
    from var import distro
    distro = reload(distro)
    print ("\tDistro name:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.name+" ("+distro.code+")"+process_colors.get_colors())
    print ("\tDistro version:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.version+process_colors.get_colors())
    print ("\tDistro id:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.id+process_colors.get_colors())
    print ("\tHostname:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+get_hostname()+process_colors.get_colors())
    print ("\tKernel name:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_magic+ " ("+k_header_code+")"+process_colors.get_colors())
    print ("\tKernel type:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+"Hight microkernel"+process_colors.get_colors())
    print ("\tKernel version:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_version+process_colors.get_colors())
    print ("\tLicense:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_license+process_colors.get_colors())

def out(values):
    for i in values:
        print(i.replace("\\n","\n").replace("\\a","\a").replace("\\b","\b").replace("\\f","\f").replace("\\r","\r").replace("\\t","\t").replace("\\v","\v").replace("\\s"," "),end=' ')
def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." + process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." +process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.mkdir(root + "/" + i)
def rmdir(values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": isn't a directory." + process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                shutil.rmtree(root + "/" + i, ignore_errors=False, onerror=None)
            else:
                print(process_colors.get_fail()   + i + ": directory not found." +process_colors.get_colors())
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()  + i + ": isn't a directory." +process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                os.rmdir(root + "/" + i)
            else:
                print(process_colors.get_fail()   + i + ": directory not found." + process_colors.get_colors())

def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.get_fail()  + i + ": isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()  + i + ": file not found." +process_colors.get_colors())
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
                    print(process_colors.get_fail() + i + ": isn't a file." + process_colors.get_colors())
                else:
                    print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_fail()   + i + ": isn't a file." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())
def license ():
    file = open ("etc/license","r")
    strv = file.read()
    file.close()
    print (strv)

def help():
    print(
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cat" +process_colors.get_colors() + "\t\t[file] ...\tShow files on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cd" + process_colors.get_colors() + "\t\t[dir]\t\tChnage directory workspace.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cp" + process_colors.get_colors() + "\t\t[src] [dist]\tCopy files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "exit/logout" + process_colors.get_colors()+ "\t\t\tExit from shell.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "ls" +process_colors.get_colors() + "\t\t[dir]\t\tList directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "license" + process_colors.get_colors() + "\t\t[dir]\t\tShow kernel license.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "mkdir" + process_colors.get_colors() + "\t\t[dir] ...\tCreate directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "mv" + process_colors.get_colors() + "\t\t[src] [dist]\tMove or rename files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "out" + process_colors.get_colors() + "\t\t[...]\t\tPrint message on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "passwd" + process_colors.get_colors() + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "pyc" +process_colors.get_colors()+ "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "reboot" + process_colors.get_colors()+ "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rm" + process_colors.get_colors() + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rmdir" + process_colors.get_colors() + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "shut" +process_colors.get_colors() + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "su" + process_colors.get_colors() + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "useradd" + process_colors.get_colors() + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userinfo" +process_colors.get_colors() + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userlist" + process_colors.get_colors() + "\t\t\tList users account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userm" + process_colors.get_colors() + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "ver" +process_colors.get_colors()+ "\t\t\t\tShow informations about kernel."
    )
def cp (values):
    if values[0].startswith("-"):
        if values[0].__contains__("r"):
            if os.path.isdir(root + "/" + values[1]):
                if os.path.isfile(root + "/" + values[2]):
                    print(process_colors.get_fail()   + values[2] + ": dest isn't a directory." +process_colors.get_colors())
                else:
                    shutil.copytree(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isfile(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": source isn't a directory." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + values[1] + ": source not found." + process_colors.get_colors())
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": dest isn't a file." + process_colors.get_colors())
            else:
                shutil.copyfile(root + "/" + values[0], root + "/" + values[1])
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.get_fail()  + values[0] + ": source isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())
def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+values[1])
    else:
        print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())
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
                    print(process_colors.get_fail()  + "Wrong password! Try agian.\n" + process_colors.get_colors())
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
        print(process_colors.get_fail()   + username + ": user already exists." +process_colors.get_colors())
def userm (username):
    if username=="root":
        print(process_colors.get_fail()  +username+ ": cannot remove root user account: Is a permanent user." + process_colors.get_colors())
    elif os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
        keep = input ("Are you going to keep this " + username+"'s files? [Y/n]: ")
        if keep=="Y" or keep=="y":
            os.remove("etc/users/"+username)
        elif keep=="N" or keep=="n" or keep=="\0":
            shutil.rmtree("desk/"+username,ignore_errors=False, onerror=None)
            os.remove("etc/users/"+username)
    else:
        print(process_colors.get_fail()   +username+ ": user not found." + process_colors.get_colors())
def passwd (username):
    if username=="root" and os.path.isdir("root") and os.path.isfile("etc/users/root"):
        shutil.copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
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
                                        process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
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
                print(process_colors.get_fail()   + "Wrong password." + process_colors.get_colors())
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
                                print(process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
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
            shutil.copyfile("etc/users/" + username, "var/switch_user.pyc")
            from var import switch_user
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
                                            process_colors.get_fail() + "Wrong password! Try agian.\n" + process_colors.get_colors())
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
                    print(process_colors.get_fail()  + "Wrong password." +process_colors.get_colors())
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
                                    print(process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
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
            print(process_colors.get_fail()   + username + ": user not found." + process_colors.get_colors())
def userinfo (username):
    if username=="root" and os.path.isdir ("root") and os.path.isfile ("etc/users/root"):
        copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + switch_user.name + process_colors.get_colors())
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "enable" +process_colors.get_colors())
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "disable" + process_colors.get_colors())
    elif os.path.isdir ("desk/"+username) and os.path.isfile("etc/users/"+username):
        copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + switch_user.name +process_colors.get_colors())
        if switch_user.admin == True:
            print("    Type:       " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "Administrator" + process_colors.get_colors())
        else:
            print("    Type:       " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "Standard" + process_colors.get_colors())
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "enable" +process_colors.get_colors())
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "disable" + process_colors.get_colors())
    elif username=="" or username==" ":
        print()
    else:
        print(process_colors.get_fail()   +username+ ": user not found." +process_colors.get_colors())
def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.get_colors())
            else:
                print(process_colors.get_path() + dir + "/" + process_colors.get_colors())
    else:
        print(process_colors.get_fail()   +path+ ": directory not found." +process_colors.get_colors())
def pyc (values):
    if values[0].startswith("-"):
        if values[0].__contains__("o"):
            if os.path.isfile(root + "/" + values[1]):
                if os.path.isdir(root + "/" + values[2]):
                    print(process_colors.get_fail()   + values[2] + ": source isn't a file." +process_colors.get_colors())
                else:
                    py_compile.compile(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isdir(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": source isn't a file." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()  + values[1] + ": source not found." +process_colors.get_colors())
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/"+str(values[0].replace(".py",""))+".pyc"):
                print(process_colors.get_fail() + str(values[0].replace(".py",""))+".pyc" + ": dest isn't a file." + process_colors.get_colors())
            else:
                py_compile.compile(root + "/" + values[0], root + "/" + str(values[0].replace(".py",""))+".pyc")
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.get_fail()   + values[0] + ": source isn't a file.." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()  + values[0] + ": source not found." +process_colors.get_colors())
def exec (filename,args):
    if os.path.isfile( "bin/" + filename + ".pyc"):
        process.clean_switch()
        copyfile("bin/" + filename + ".pyc", "var/switch_process.pyc")
        from var import switch_process
        switch_process = reload(switch_process)
        switch_process.main(args)
        process.clean_switch()
def su (user_already,username):
    if user_already==username:
        print(process_colors.get_warning() +username+ ": user already switched." + process_colors.get_colors())
    else:
        if username=="root":
            enter_password("root","#")
        elif os.path.isdir ("desk/"+username) and os.path.isfile ("etc/users/"+username):
            enter_password(username,"$")
        else:
            print(process_colors.get_fail()  + username + ": user not found." + process_colors.get_colors())
def logout():
    k_login()
def reboot():
    import vmwet
    vmwet = reload(vmwet)
def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+"\t"+user+process_colors.get_colors()+"\tActive")
        else:
            print (process_colors.get_fail()  +"\t"+user+process_colors.get_colors()+"\tInactive")
    print(process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "\troot"+process_colors.get_colors()+ "\tActive")
