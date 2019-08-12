def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
        else:
            print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)