def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.color(1,process_colors.white,40)+"\t"+user+process_colors.color(0,process_colors.white,40)+"\tActive")
        else:
            print (process_colors.color(0,process_colors.red,40) +"\t"+user+process_colors.color(0,process_colors.white,40)+"\tInactive")
    print(process_colors.color(1,process_colors.white,40) + "\troot"+process_colors.color(0,process_colors.white,40) + "\tActive")