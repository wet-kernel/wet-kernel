
def help():
    print(
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cat" +process_colors.get_colors() + "\t\t[file] ...\tShow files on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cd" + process_colors.get_colors() + "\t\t[dir]\t\tChnage directory workspace.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "cp" + process_colors.get_colors() + "\t\t[src] [dist]\tCopy files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "exit/logout" + process_colors.get_colors()+ "\t\t\tExit from shell.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "ls" +process_colors.get_colors() + "\t\t[dir]\t\tList directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "license" + process_colors.get_colors() + "\t\t[dir]\t\tShow kernel license.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "mkdir" + process_colors.get_colors() + "\t\t[dir] ...\tCreate directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "mv" + process_colors.get_colors() + "\t\t[src] [dist]\tMove or rename files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "out" + process_colors.get_colors() + "\t\t[...]\t\tPrint message on screen.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "passwd" + process_colors.get_colors() + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "pyc" +process_colors.get_colors()+ "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "reboot" + process_colors.get_colors()+ "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rm" + process_colors.get_colors() + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rmdir" + process_colors.get_colors() + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "shut" +process_colors.get_colors() + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "su" + process_colors.get_colors() + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "useradd" + process_colors.get_colors() + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userinfo" +process_colors.get_colors() + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userlist" + process_colors.get_colors() + "\t\t\tList users account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userm" + process_colors.get_colors() + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "ver" +process_colors.get_colors()+ "\t\t\t\tShow informations about kernel."
    )