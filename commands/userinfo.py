def userinfo (username):
    if username=="root" and os.path.isdir ("root") and os.path.isfile ("etc/users/root"):
        copyfile("etc/users/" + username, "etc/switch_user.pyc")
        from etc import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,40) + switch_user.name + process_colors.color(0,process_colors.white,40))
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,40) + "enable" +process_colors.color(0,process_colors.white,40))
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,40) + "disable" + process_colors.color(0,process_colors.white,40))
    elif os.path.isdir ("desk/"+username) and os.path.isfile("etc/users/"+username):
        copyfile("etc/users/" + username, "etc/switch_user.pyc")
        from etc import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,40) + switch_user.name +process_colors.color(0,process_colors.white,40))
        if switch_user.admin == True:
            print("    Type:       " + process_colors.color(1,process_colors.white,40) + "Administrator" + process_colors.color(0,process_colors.white,40))
        else:
            print("    Type:       " + process_colors.color(1,process_colors.white,40) + "Standard" + process_colors.color(0,process_colors.white,40))
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,40) + "enable" +process_colors.color(0,process_colors.white,40))
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,40) + "disable" + process_colors.color(0,process_colors.white,40))
    elif username=="" or username==" ":
        print()
    else:
        print(process_colors.color(0,process_colors.red,40)  +username+ ": user not found." +process_colors.color(0,process_colors.white,40))