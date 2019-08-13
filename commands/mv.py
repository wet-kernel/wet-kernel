def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+dest)
    else:
        print(process_colors.color(0,process_colors.red,40)  + values[0] + ": source not found." + process_colors.color(0,process_colors.white,40))