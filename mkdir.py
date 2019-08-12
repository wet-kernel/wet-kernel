def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": file exists." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.WARNING + i + ": directory exists." + process_colors.ENDC)
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": file exists." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.WARNING + i + ": directory exists." + process_colors.ENDC)
            else:
                os.mkdir(root + "/" + i)