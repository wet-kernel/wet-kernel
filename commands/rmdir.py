def rmdir(values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": isn't a directory." + process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                shutil.rmtree(root + "/" + i, ignore_errors=False, onerror=None)
            else:
                print(process_colors.get_fail()   + i + ": directory not found." +process_colors.get_colors())
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()  + i + ": isn't a directory." +process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                os.rmdir(root + "/" + i)
            else:
                print(process_colors.get_fail()   + i + ": directory not found." + process_colors.get_colors())
