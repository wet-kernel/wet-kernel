

def enter_password(username,command_symbol):
    user_file = "etc/users/"+username
    copyfile (user_file,"etc/switch_user.pyc")
    from etc import switch_user
    switch_user = reload(switch_user)
    i = 1
    while i<6:
        if switch_user.security == True:
            password = input ("Enter "+switch_user.name+"'s password: ")
            if password==switch_user.code:
                k_shell(switch_user.name,command_symbol,"/")
            else:
                print (process_colors.color(0,process_colors.red,40) +"Wrong password.\n"+process_colors.color(0,process_colors.white,40))
                i = i + 1
        else:
            k_shell(switch_user.name,command_symbol,"/")