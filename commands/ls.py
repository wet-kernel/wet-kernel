def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.ENDC)
            else:
                print(process_colors.BOLD + process_colors.OKBLUE + dir + "/" + process_colors.ENDC)
    else:
        print(process_colors.FAIL +path+ ": directory not found." + process_colors.ENDC)