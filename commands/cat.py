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
                    print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
                else:
                    print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a file." + process_colors.ENDC)
            else:
                print(process_colors.FAIL + i + ": file not found." + process_colors.ENDC)