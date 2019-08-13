def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.color(0,process_colors.white,40))
            else:
                print(process_colors.color(1,process_colors.blue,40) + dir + "/" + process_colors.color(0,process_colors.white,40))
    else:
        print(process_colors.color(0,process_colors.red,40)  +path+ ": directory not found." +process_colors.color(0,process_colors.white,40))