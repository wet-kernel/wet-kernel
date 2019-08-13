def userm (username):
    if username=="root":
        print(process_colors.color(0,process_colors.red,40)  +username+ ": cannot remove root user account: Is a permanent user." + process_colors.color(0,process_colors.white,40))
    elif os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
        keep = input ("Are you going to keep this " + username+"'s files? [Y/n]: ")
        if keep=="Y" or keep=="y":
            os.remove("etc/users/"+username)
        elif keep=="N" or keep=="n" or keep=="\0":
            shutil.rmtree("desk/"+username,ignore_errors=False, onerror=None)
            os.remove("etc/users/"+username)
    else:
        print(process_colors.color(0,process_colors.red,40)  +username+ ": user not found." + process_colors.color(0,process_colors.white,40))