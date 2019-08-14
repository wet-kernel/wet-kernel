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