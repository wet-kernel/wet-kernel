
def help():
    print(
        "\t" + process_colors.BOLD + "cat" + process_colors.ENDC + "\t\t[file] ...\tShow files on screen.\n" +
        "\t" + process_colors.BOLD + "cd" + process_colors.ENDC + "\t\t[dir]\t\tChnage directory workspace.\n" +
        "\t" + process_colors.BOLD + "cp" + process_colors.ENDC + "\t\t[src] [dist]\tCopy files.\n" +
        "\t" + process_colors.BOLD + "exit/logout" + process_colors.ENDC + "\t\t\tExit from shell.\n" +
        "\t" + process_colors.BOLD + "ls" + process_colors.ENDC + "\t\t[dir]\t\tList directory.\n" +
        "\t" + process_colors.BOLD + "mkdir" + process_colors.ENDC + "\t\t[dir] ...\tCreate directory.\n" +
        "\t" + process_colors.BOLD + "mv" + process_colors.ENDC + "\t\t[src] [dist]\tMove or rename files.\n" +
        "\t" + process_colors.BOLD + "out" + process_colors.ENDC + "\t\t[...]\t\tPrint message on screen.\n" +
        "\t" + process_colors.BOLD + "passwd" + process_colors.ENDC + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.BOLD + "pyc" + process_colors.ENDC + "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.BOLD + "reboot" + process_colors.ENDC + "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.BOLD + "rm" + process_colors.ENDC + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.BOLD + "rmdir" + process_colors.ENDC + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.BOLD + "shut" + process_colors.ENDC + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.BOLD + "su" + process_colors.ENDC + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.BOLD + "useradd" + process_colors.ENDC + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.BOLD + "userinfo" + process_colors.ENDC + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.BOLD + "userlist" + process_colors.ENDC + "\t\t\tList users account.\n" +
        "\t" + process_colors.BOLD + "userm" + process_colors.ENDC + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.BOLD + "ver" + process_colors.ENDC + "\t\t\t\tShow informations about kernel."
    )