def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+"\t"+user+process_colors.get_colors()+"\tActive")
        else:
            print (process_colors.get_fail()  +"\t"+user+process_colors.get_colors()+"\tInactive")
    print(process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "\troot"+process_colors.get_colors()+ "\tActive")