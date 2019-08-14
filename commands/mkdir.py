def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." + process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." +process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.mkdir(root + "/" + i)