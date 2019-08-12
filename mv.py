def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+dest)
    else:
        print(process_colors.FAIL + values[0] + ": source not found." + process_colors.ENDC)