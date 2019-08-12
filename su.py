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