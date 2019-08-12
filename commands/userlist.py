def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.BOLD+"    "+user+process_colors.ENDC+"\tActive")
        else:
            print (process_colors.BOLD+process_colors.FAIL+"    "+user+process_colors.ENDC+"    Inactive")
    print(process_colors.BOLD + "    root"+process_colors.ENDC + "\tActive")