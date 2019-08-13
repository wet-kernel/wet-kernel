def su (user_already,username):
    if user_already==username:
        print(process_colors.color(0,process_colors.yellow,40) +username+ ": user already switched." + process_colors.color(0,process_colors.white,40))
    else:
        if username=="root":
            enter_password("root","#")
        elif os.path.isdir ("desk/"+username) and os.path.isfile ("etc/users/"+username):
            enter_password(username,"$")
        else:
            print(process_colors.color(0,process_colors.red,40)  + username + ": user not found." + process_colors.color(0,process_colors.white,40))