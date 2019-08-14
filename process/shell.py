

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
    elif command == "license":
        license()
    elif commandline[0] == "pack":
        pack(commandline[1:])
    elif commandline[0] == "unpack":
        unpack(commandline[1:])
    elif os.path.isfile("bin/" + commandline[0] + ".pyc"):
        exec(commandline[0], commandline[1:])
    else:
        print(process_colors.get_fail()  + commandline[0] + ": command not found." + process_colors.get_colors())

def k_shell(username,command_symbol,path):
    print()
    process.show_start_process("shell")
    print()
    while True:
        color_prompt =process_colors.get_colors()
        color_path =process_colors.get_colors()
        if username=="root":
            color_prompt = process_colors.get_colors()
            color_path = process_colors.get_colors()
        else:
            color_prompt = process_colors.get_prompt()
            color_path = process_colors.get_path()

        command = input (color_prompt+username+"@"+get_hostname()+process_colors.color(process_colors.get_style(),process_colors.white,process_colors.get_bgcolor())+":"+color_path+path+process_colors.get_colors()+ command_symbol+" ")
        commandline = command.split(" ")

        if commandline[0] == "cd":
            for i in commandline[1:]:
                if commandline[1]=="" or commandline[1]==" ":
                    path = ""
                elif commandline[1].startswith("/"):
                    if os.path.isdir(root + "/" + commandline[1]):
                        path = commandline[1]
                    else:
                        print(process_colors.get_fail()  + commandline[1] + ": directory not found." + process_colors.get_colors())
                else:
                    if os.path.isdir(root+"/"+path+"/"+commandline[1]):
                        if path == "/":
                            path = path + commandline[1]
                        else:
                            path = path + "/" + commandline[1]
                    else:
                        print(process_colors.get_fail()  + commandline[1] + ": directory not found." +process_colors.get_colors())
        else:
            terminal(commandline,command,username,command_symbol,path)