def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.get_fail()  + i + ": isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()  + i + ": file not found." +process_colors.get_colors())