def pyc (values):
    if values[0].startswith("-"):
        if values[0].__contains__("o"):
            if os.path.isfile(root + "/" + values[1]):
                if os.path.isdir(root + "/" + values[2]):
                    print(process_colors.get_fail()   + values[2] + ": source isn't a file." +process_colors.get_colors())
                else:
                    py_compile.compile(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isdir(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": source isn't a file." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()  + values[1] + ": source not found." +process_colors.get_colors())
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/"+str(values[0].replace(".py",""))+".pyc"):
                print(process_colors.get_fail() + str(values[0].replace(".py",""))+".pyc" + ": dest isn't a file." + process_colors.get_colors())
            else:
                py_compile.compile(root + "/" + values[0], root + "/" + str(values[0].replace(".py",""))+".pyc")
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.get_fail()   + values[0] + ": source isn't a file.." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()  + values[0] + ": source not found." +process_colors.get_colors())