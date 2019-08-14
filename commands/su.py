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