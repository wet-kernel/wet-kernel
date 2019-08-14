import shutil

def pack (values):
    if values[0]=="-t":
        if values[1]=="zip":
            if values[2].startswith("-"):
                if values[2].__contains__("-o"):
                    if os.path.isdir(root + "/" + values[4]):
                        shutil.make_archive(root + "/" + values[3], "zip", root + "/" + values[4])
                    else:
                        print(process_colors.get_fail() + values[3] + ": directory not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isdir(root + "/" + values[2]):
                    shutil.make_archive(root + "/" + values[2], "zip", root + "/" + values[2])
                else:
                    print(process_colors.get_fail() + values[2] + ": directory not found.")
        elif values[1]=="tar":
            if values[2].startswith("-"):
                if values[2].__contains__("-o"):
                    if os.path.isdir(root + "/" + values[4]):
                        shutil.make_archive(root + "/" + values[3], "tar", root + "/" + values[4])
                    else:
                        print(process_colors.get_fail() + values[3] + ": directory not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isdir(root + "/" + values[2]):
                    shutil.make_archive(root + "/" + values[2], "tar", root + "/" + values[2])
                else:
                    print(process_colors.get_fail() + values[2] + ": directory not found.")
        elif values[1]=="xztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-o"):
                    if os.path.isdir(root + "/" + values[4]):
                        shutil.make_archive(root + "/" + values[3], "xztar", root + "/" + values[4])
                    else:
                        print(process_colors.get_fail() + values[3] + ": directory not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isdir(root + "/" + values[2]):
                    shutil.make_archive(root + "/" + values[2], "xztar", root + "/" + values[2])
                else:
                    print(process_colors.get_fail() + values[2] + ": directory not found.")
        elif values[1] == "gztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-o"):
                    if os.path.isdir(root + "/" + values[4]):
                        shutil.make_archive(root + "/" + values[3], "gztar", root + "/" + values[4])
                    else:
                        print(process_colors.get_fail() + values[3] + ": directory not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isdir(root + "/" + values[2]):
                    shutil.make_archive(root + "/" + values[2], "gztar", root + "/" + values[2])
                else:
                    print(process_colors.get_fail() + values[2] + ": directory not found.")
        elif values[1] == "bztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-o"):
                    if os.path.isdir(root + "/" + values[4]):
                        shutil.make_archive(root + "/" + values[3], "bztar", root + "/" + values[4])
                    else:
                        print(process_colors.get_fail() + values[3] + ": directory not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isdir(root + "/" + values[2]):
                    shutil.make_archive(root + "/" + values[2], "bztar", root + "/" + values[2])
                else:
                    print(process_colors.get_fail() + values[2] + ": directory not found.")
        else:
            print(process_colors.get_fail() + values[1] + ": archive type not found.")
    else:
        print(process_colors.get_fail() + values[0] + ": option not found.")

def unpack (values):
    if values[0] == "-t":
        if values[1] == "zip":
            if values[2].startswith("-"):
                if values[2].__contains__("-d"):
                    if os.path.isfile(root + "/" + values[3] + ".zip"):
                        shutil.unpack_archive(root + "/" + values[3] + ".zip", root + "/" + values[4], "zip")
                    else:
                        print(process_colors.get_fail() + values[3] + ": archive not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isfile(root + "/" + values[2] + ".zip"):
                    shutil.unpack_archive(root + "/" + values[2] + ".zip", root + "/" + values[2], "zip")
                else:
                    print(process_colors.get_fail() + values[2] + ": archive not found.")
        elif values[1] == "tar":
            if values[2].startswith("-"):
                if values[2].__contains__("-d"):
                    if os.path.isfile(root + "/" + values[3] + ".tar"):
                        shutil.unpack_archive(root + "/" + values[3] + ".tar", root + "/" + values[4], "tar")
                    else:
                        print(process_colors.get_fail() + values[3] + ": archive not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isfile(root + "/" + values[2] + ".tar"):
                    shutil.unpack_archive(root + "/" + values[2] + ".tar", root + "/" + values[2], "tar")
                else:
                    print(process_colors.get_fail() + values[2] + ": archive not found.")
        elif values[1] == "xztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-d"):
                    if os.path.isfile(root + "/" + values[3] + ".tar.xz"):
                        shutil.unpack_archive(root + "/" + values[3] + ".tar.xz", root + "/" + values[4], "xztar")
                    else:
                        print(process_colors.get_fail() + values[3] + ": archive not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isfile(root + "/" + values[2] + ".tar.xz"):
                    shutil.unpack_archive(root + "/" + values[2] + ".tar.xz", root + "/" + values[2], "xztar")
                else:
                    print(process_colors.get_fail() + values[2] + ": archive not found.")
        elif values[1] == "gztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-d"):
                    if os.path.isfile(root + "/" + values[3] + ".tar.gz"):
                        shutil.unpack_archive(root + "/" + values[3] + ".tar.gz", root + "/" + values[4], "gztar")
                    else:
                        print(process_colors.get_fail() + values[3] + ": archive not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isfile(root + "/" + values[2] + ".tar.gz"):
                    shutil.unpack_archive(root + "/" + values[2] + ".tar.gz", root + "/" + values[2], "gztar")
                else:
                    print(process_colors.get_fail() + values[2] + ": archive not found.")
        elif values[1] == "bztar":
            if values[2].startswith("-"):
                if values[2].__contains__("-d"):
                    if os.path.isfile(root + "/" + values[3] + ".tar.bz2"):
                        shutil.unpack_archive(root + "/" + values[3] + ".tar.bz2", root + "/" + values[4], "bztar")
                    else:
                        print(process_colors.get_fail() + values[3] + ": archive not found.")
                else:
                    print(process_colors.get_fail() + values[2] + ": option not found.")
            else:
                if os.path.isfile(root + "/" + values[2] + ".tar.bz2"):
                    shutil.unpack_archive(root + "/" + values[2] + ".tar.bz2", root + "/" + values[2], "bztar")
                else:
                    print(process_colors.get_fail() + values[2] + ": archive not found.")
        else:
            print(process_colors.get_fail() + values[1] + ": archive type not found.")
    else:
        print(process_colors.get_fail() + values[2] + ": option not found.")