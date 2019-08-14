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