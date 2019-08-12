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