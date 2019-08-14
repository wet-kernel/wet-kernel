def cp (values):
    if values[0].startswith("-"):
        if values[0].__contains__("r"):
            if os.path.isdir(root + "/" + values[1]):
                if os.path.isfile(root + "/" + values[2]):
                    print(process_colors.get_fail()   + values[2] + ": dest isn't a directory." +process_colors.get_colors())
                else:
                    shutil.copytree(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isfile(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": source isn't a directory." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + values[1] + ": source not found." + process_colors.get_colors())
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": dest isn't a file." + process_colors.get_colors())
            else:
                shutil.copyfile(root + "/" + values[0], root + "/" + values[1])
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.get_fail()  + values[0] + ": source isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())