def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.get_colors())
            else:
                print(process_colors.get_path() + dir + "/" + process_colors.get_colors())
    else:
        print(process_colors.get_fail()   +path+ ": directory not found." +process_colors.get_colors())