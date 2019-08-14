def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+values[1])
    else:
        print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())