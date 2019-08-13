def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.color(0,process_colors.red,40)  + i + ": isn't a file." + process_colors.color(0,process_colors.white,40))
        else:
            print(process_colors.color(0,process_colors.red,40)  + i + ": file not found." +process_colors.color(0,process_colors.white,40))