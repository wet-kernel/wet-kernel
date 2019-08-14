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