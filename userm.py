def userm (username):
    if username=="root":
        print(process_colors.FAIL +username+ ": cannot remove root user account: Is a permanent user." + process_colors.ENDC)
    elif os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
        keep = input ("Are you going to keep this " + username+"'s files? [Y/n]: ")
        if keep=="Y" or keep=="y":
            os.remove("etc/users/"+username)
        elif keep=="N" or keep=="n" or keep=="\0":
            shutil.rmtree("desk/"+username,ignore_errors=False, onerror=None)
            os.remove("etc/users/"+username)
    else:
        print(process_colors.FAIL +username+ ": user not found." + process_colors.ENDC)