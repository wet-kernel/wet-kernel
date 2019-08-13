def cp (values):
    if values[0].startswith("-"):
        if values[0].__contains__("r"):
            if os.path.isdir(root + "/" + values[1]):
                if os.path.isfile(root + "/" + values[2]):
                    print(process_colors.color(0,process_colors.red,40)  + values[2] + ": dest isn't a directory." +process_colors.color(0,process_colors.white,40))
                else:
                    shutil.copytree(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isfile(root + "/" + values[1]):
                print(process_colors.color(0,process_colors.red,40)  + values[1] + ": source isn't a directory." + process_colors.color(0,process_colors.white,40))
            else:
                print(process_colors.color(0,process_colors.red,40)  + values[1] + ": source not found." + process_colors.color(0,process_colors.white,40))
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/" + values[1]):
                print(process_colors.color(0,process_colors.red,40)  + values[1] + ": dest isn't a file." + process_colors.color(0,process_colors.white,40))
            else:
                shutil.copyfile(root + "/" + values[0], root + "/" + values[1])
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.color(0,process_colors.red,40)  + values[0] + ": source isn't a file." + process_colors.color(0,process_colors.white,40))
        else:
            print(process_colors.color(0,process_colors.red,40)  + values[0] + ": source not found." + process_colors.color(0,process_colors.white,40))