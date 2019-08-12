def rmdir(values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a directory." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                shutil.rmtree(root + "/" + i, ignore_errors=False, onerror=None)
            else:
                print(process_colors.FAIL + i + ": directory not found." + process_colors.ENDC)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.FAIL + i + ": isn't a directory." + process_colors.ENDC)
            elif os.path.isdir(root + "/" + i):
                os.rmdir(root + "/" + i)
            else:
                print(process_colors.FAIL + i + ": directory not found." + process_colors.ENDC)
