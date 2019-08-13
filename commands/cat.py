def cat (values):
    if values[0].startswith("-"):
        if values[0].__contains__("b"):
            for i in values[1:]:
                if os.path.isfile(root + "/" + i):
                    file = open(root + "/" + i, "rb")
                    strv = file.read()
                    file.close()
                    print(strv)
                elif os.path.isdir(root + "/" + i):
                    print(process_colors.color(0,process_colors.red,40) + i + ": isn't a file." + process_colors.color(0,process_colors.white,40))
                else:
                    print(process_colors.color(0,process_colors.red,40)  + i + ": file not found." + process_colors.color(0,process_colors.white,40))
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.color(0,process_colors.red,40)  + i + ": isn't a file." + process_colors.color(0,process_colors.white,40))
            else:
                print(process_colors.color(0,process_colors.red,40)  + i + ": file not found." + process_colors.color(0,process_colors.white,40))