
def get_permissions (username,permission):
    if username=="root":
        return True
    else:
        if switch_user.admin==True:
            if switch_user.security == True:
                password = input("Enter " + switch_user.name + "'s password: ")
                if password == switch_user.code:
                    return True
                else:
                    print(process_colors.FAIL + "Wrong password.\n" + process_colors.ENDC)
                    return False
            else:
                return True
        else:
            print(process_colors.FAIL +permission+ ": Permission denied." + process_colors.ENDC)
            return False