def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.color(0,process_colors.red,40)  + i + ": file exists." + process_colors.color(0,process_colors.white,40))
            elif os.path.isdir(root + "/" + i):
                print(process_colors.color(0,process_colors.yellow,40) + i + ": directory exists." + process_colors.color(0,process_colors.white,40))
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.color(0,process_colors.red,40)  + i + ": file exists." +process_colors.color(0,process_colors.white,40))
            elif os.path.isdir(root + "/" + i):
                print(process_colors.color(0,process_colors.yellow,40) + i + ": directory exists." + process_colors.color(0,process_colors.white,40))
            else:
                os.mkdir(root + "/" + i)