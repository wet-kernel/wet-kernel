
def help():
    print(
        "\t" + process_colors.color(1,process_colors.white,40) + "cat" +process_colors.color(0,process_colors.white,40) + "\t\t[file] ...\tShow files on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "cd" + process_colors.color(0,process_colors.white,40) + "\t\t[dir]\t\tChnage directory workspace.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "cp" + process_colors.color(0,process_colors.white,40) + "\t\t[src] [dist]\tCopy files.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "exit/logout" + process_colors.color(0,process_colors.white,40)+ "\t\t\tExit from shell.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "ls" + process_colors.color(0,process_colors.white,40) + "\t\t[dir]\t\tList directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "mkdir" + process_colors.color(0,process_colors.white,40) + "\t\t[dir] ...\tCreate directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "mv" + process_colors.color(0,process_colors.white,40) + "\t\t[src] [dist]\tMove or rename files.\n" +
        "\t" + process_colors.color(1,process_colors.white,40)+ "out" + process_colors.color(0,process_colors.white,40) + "\t\t[...]\t\tPrint message on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "passwd" + process_colors.color(0,process_colors.white,40) + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.color(1,process_colors.white,40)+ "pyc" +process_colors.color(0,process_colors.white,40)+ "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.color(1,process_colors.white,40)+ "reboot" + process_colors.color(0,process_colors.white,40)+ "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "rm" + process_colors.color(0,process_colors.white,40) + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "rmdir" + process_colors.color(0,process_colors.white,40) + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "shut" +process_colors.color(0,process_colors.white,40) + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "su" + process_colors.color(0,process_colors.white,40) + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "useradd" + process_colors.color(0,process_colors.white,40) + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "userinfo" + process_colors.color(0,process_colors.white,40) + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "userlist" + process_colors.color(0,process_colors.white,40) + "\t\t\tList users account.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "userm" + process_colors.color(0,process_colors.white,40) + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,40) + "ver" + process_colors.color(0,process_colors.white,40)+ "\t\t\t\tShow informations about kernel."
    )