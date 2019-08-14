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
                    print(process_colors.get_fail() + i + ": isn't a file." + process_colors.get_colors())
                else:
                    print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_fail()   + i + ": isn't a file." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())