
k_header_magic = "wet"
k_header_version = "0.27"
k_header_code = "test"
k_header_license = "GPL v3"

import os, sys, shutil, py_compile
from shutil import copyfile
from importlib import reload

class process_colors:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37

    style_none = 0
    style_bold = 1
    style_underline = 2
    style_negative1 = 3
    style_negative2 = 5

    bg_black = 40
    bg_red = 41
    bg_green = 42
    bg_yellow = 43
    bg_blue = 44
    bg_purple = 45
    bg_cyan = 46
    bg_white = 47

    def color (style,text,background):
        return "\033["+str(style)+";"+str(text)+";"+str(background)+"m"

    def get_colors ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        style = color.style
        fgcolor = color.fgcolor
        bgcolor = color.bgcolor
        return "\033["+str(style)+";"+str(fgcolor)+";"+str(bgcolor)+"m"

    def get_style ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.style
        return strv

    def get_fgcolor ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.fgcolor
        return strv

    def get_bgcolor ():
        py_compile.compile("etc/console/color","var/color.pyc")
        from var import color
        color = reload(color)
        strv = color.bgcolor
        return strv

    def get_warning():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.warning_style) + ";" + str(color.warning_fgcolor) + ";" + str(color.warning_bgcolor) + "m"
        return strv

    def get_path():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.path_style) + ";" + str(color.path_fgcolor) + ";" + str(color.path_bgcolor) + "m"
        return strv

    def get_prompt():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.prompt_style) + ";" + str(color.prompt_fgcolor) + ";" + str(color.prompt_bgcolor) + "m"
        return strv

    def get_fail():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.fail_style) + ";" + str(color.fail_fgcolor) + ";" + str(color.fail_bgcolor) + "m"
        return strv

    def get_ok():
        py_compile.compile("etc/console/color", "var/color.pyc")
        from var import color
        color = reload(color)
        strv =  "\033[" + str(color.ok_style) + ";" + str(color.ok_fgcolor) + ";" + str(color.ok_bgcolor) + "m"
        return strv
class process:
    def show_start_process(process_name):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Start " + process_name + " process ...")

    def show_fail_process(process_name):
        print("[" + process_colors.get_fail()   + " Fail " +process_colors.get_colors() + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] End " + process_name + " process ...")

    def show_power_on ():
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.get_fail()   + " STOP " +process_colors.get_colors() + "] Stop the kernel ...")

    def show_power_off ():
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power off the kernel ...")

    def show_reboot():
        print("[" + process_colors.get_ok() + " OK " +process_colors.get_colors() + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Clean switch "+switch+" ...")

    def clean_switch():
        if os.path.isfile ("var/switch_process.pyc"):
            os.remove ("var/switch_process.pyc")
        if os.path.isfile ("var/switch_user.pyc"):
            os.remove ("var/switch_user.pyc")

def show_issue():
    issue_filename = "etc/issue"
    file = open (issue_filename,"r")
    strv = file.read()
    file.close()
    print (strv)
def get_hostname():
    hostname_filename = "etc/hostname"
    file = open (hostname_filename,"r")
    strv = file.read()
    file.close()
    return strv


def enter_password(username,command_symbol):
    user_file = "etc/users/"+username
    copyfile (user_file,"var/switch_user.pyc")
    from var import switch_user
    switch_user = reload(switch_user)
    i = 1
    while i<6:
        if switch_user.security == True:
            password = input ("Enter "+switch_user.name+"'s password: ")
            if password==switch_user.code:
                k_shell(switch_user.name,command_symbol,"/")
            else:
                print (process_colors.get_fail()  +"Wrong password.\n"+process_colors.get_colors())
                i = i + 1
        else:
            k_shell(switch_user.name,command_symbol,"/")

def get_permissions (username,permission):
    if username=="root":
        return True
    else:
        if switch_user.admin==True:
            if switch_user.security == True:
                password = input("Enter " + switch_user.name + "'s password: ")
                if password == switch_user.code:
                    return True
                else:
                    print(process_colors.get_fail()   + "Wrong password.\n" + process_colors.get_colors())
                    return False
            else:
                return True
        else:
            print(process_colors.get_fail()  +permission+ ": Permission denied." + process_colors.get_colors())
            return False

def shut():
    file = open ("etc/process","r")
    i = int(file.readline())
    file.close()
    os.rmdir("var/shell/" + str(i))
    file = open ("etc/process","w")
    i = i - 1
    file.write(str(i))
    file.close()
    process.show_end_process("shell")
    process.show_power_off()
    exit(0)
def ver():
    py_compile.compile("etc/distro", "var/distro.pyc")
    from var import distro
    distro = reload(distro)
    print ("\tDistro name:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.name+" ("+distro.code+")"+process_colors.get_colors())
    print ("\tDistro version:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.version+process_colors.get_colors())
    print ("\tDistro id:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+distro.id+process_colors.get_colors())
    print ("\tHostname:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+get_hostname()+process_colors.get_colors())
    print ("\tKernel name:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_magic+ " ("+k_header_code+")"+process_colors.get_colors())
    print ("\tKernel type:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+"Hight microkernel"+process_colors.get_colors())
    print ("\tKernel version:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_version+process_colors.get_colors())
    print ("\tLicense:\t"+process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+k_header_license+process_colors.get_colors())
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

def out(values):
    for i in values:
        print(i.replace("\\n","\n").replace("\\a","\a").replace("\\b","\b").replace("\\f","\f").replace("\\r","\r").replace("\\t","\t").replace("\\v","\v").replace("\\s"," "),end=' ')
def mkdir (values):
    if values[0]=="-p":
        for i in values[1:]:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." + process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.makedirs(root + "/" + i)
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                print(process_colors.get_fail()   + i + ": file exists." +process_colors.get_colors())
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_warning() + i + ": directory exists." + process_colors.get_colors())
            else:
                os.mkdir(root + "/" + i)
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

def rm (values):
    for i in values:
        if os.path.isfile(root+"/"+i):
            os.remove (root+"/"+i)
        elif os.path.isdir (root+"/"+i):
            print(process_colors.get_fail()  + i + ": isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()  + i + ": file not found." +process_colors.get_colors())
def cat (values):
    if values[0].startswith("-"):
        if values[0].__contains__("b"):
            for i in values[1:]:
                if os.path.isfile(root + "/" + i):
                    file = open(root + "/" + i, "rb")
                    strv = file.read()
                    file.close()
                    print(strv)
                elif os.path.isdir(root + "/" + i):
                    print(process_colors.get_fail() + i + ": isn't a file." + process_colors.get_colors())
                else:
                    print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())
    else:
        for i in values:
            if os.path.isfile(root + "/" + i):
                file = open(root + "/" + i, "r")
                strv = file.read()
                file.close()
                print(strv)
            elif os.path.isdir(root + "/" + i):
                print(process_colors.get_fail()   + i + ": isn't a file." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + i + ": file not found." + process_colors.get_colors())
def license ():
    file = open ("etc/license","r")
    strv = file.read()
    file.close()
    print (strv)

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
        "\t" + process_colors.color(1, process_colors.white,process_colors.get_bgcolor()) + "pack" + process_colors.get_colors() + "\t\t[option] [...]\tCreate archives (zip, tar, xztar, etc).\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "passwd" + process_colors.get_colors() + "\t\t[user]\t\tAccount settings.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "pyc" +process_colors.get_colors()+ "\t\t[src] [dest]\tPython compile.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+ "reboot" + process_colors.get_colors()+ "\t\t\t\tReboot the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rm" + process_colors.get_colors() + "\t\t[file] ...\tRemove files.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "rmdir" + process_colors.get_colors() + "\t\t[dir] ...\tRemove empty directory.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "shut" +process_colors.get_colors() + "\t\t\t\tShutdown the kernel.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "su" + process_colors.get_colors() + "\t\t[user]\t\tSwitch an user account.\n" +
        "\t" + process_colors.color(1, process_colors.white,process_colors.get_bgcolor()) + "unpack" + process_colors.get_colors() + "\t\t[option] [...]\tExtract archives (zip, tar, xztar, etc).\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "useradd" + process_colors.get_colors() + "\t\t[user]\t\tCreate an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userinfo" +process_colors.get_colors() + "\t[user]\t\tShow informations about an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userlist" + process_colors.get_colors() + "\t\t\tList users account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "userm" + process_colors.get_colors() + "\t\t[user]\t\tRemove an user account.\n" +
        "\t" + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "ver" +process_colors.get_colors()+ "\t\t\t\tShow informations about kernel.\n"
    )
def cp (values):
    if values[0].startswith("-"):
        if values[0].__contains__("r"):
            if os.path.isdir(root + "/" + values[1]):
                if os.path.isfile(root + "/" + values[2]):
                    print(process_colors.get_fail()   + values[2] + ": dest isn't a directory." +process_colors.get_colors())
                else:
                    shutil.copytree(root + "/" + values[1], root + "/" + values[2])
            elif os.path.isfile(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": source isn't a directory." + process_colors.get_colors())
            else:
                print(process_colors.get_fail()   + values[1] + ": source not found." + process_colors.get_colors())
    else:
        if os.path.isfile(root + "/" + values[0]):
            if os.path.isdir(root + "/" + values[1]):
                print(process_colors.get_fail()   + values[1] + ": dest isn't a file." + process_colors.get_colors())
            else:
                shutil.copyfile(root + "/" + values[0], root + "/" + values[1])
        elif os.path.isdir(root + "/" + values[0]):
            print(process_colors.get_fail()  + values[0] + ": source isn't a file." + process_colors.get_colors())
        else:
            print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())
def mv (values):
    if os.path.isfile(root+"/"+values[0]):
        os.rename(root+"/"+values[0],root+"/"+values[1])
    else:
        print(process_colors.get_fail()   + values[0] + ": source not found." + process_colors.get_colors())
def useradd (username):
    if not (os.path.isdir("desk/"+username) or os.path.isfile("etc/users/"+username)):
        admin = input("Choose user type [A/S]: ")
        if admin=="A" or admin=="a":
            file = open("etc/users/" + username + ".py", "w")
            file.write("admin = True\n")
            file.close()
        elif admin=="S" or admin=="s":
            file = open("etc/users/" + username + ".py", "w")
            file.write("admin = False\n")
            file.close()
        security = input("Choose user security [T/f]: ")
        file = open("etc/users/" + username + ".py", "a")
        file.write("name = \"" + username + "\"\n")
        if security=="T" or security=="t":
            while True:
                password = input ("Set user a new password: ")
                code = input ("Confirm a new password: ")
                if password==code:
                    file.write("security = True\n")
                    file.write("code = \"" + password + "\"")
                    file.close()
                    break
                else:
                    print(process_colors.get_fail()  + "Wrong password! Try agian.\n" + process_colors.get_colors())
        elif security=="f" or security=="F" or security=="\0":
            file.write("security = False\n")
            file.close()
        correct = input ("Is this information correct? [Y/n]: ")
        if correct=="n" or correct=="N" or correct=="\0":
            file.close()
            os.remove ("etc/users/"+username+".py")
        elif correct=="Y" or correct=="y":
            file.close()
            src = "etc/users/"+username+".py"
            dest = "etc/users/"+username
            py_compile.compile(src,dest)
            os.remove(src)
            os.mkdir ("desk/"+username)
    else:
        print(process_colors.get_fail()   + username + ": user already exists." +process_colors.get_colors())
def userm (username):
    if username=="root":
        print(process_colors.get_fail()  +username+ ": cannot remove root user account: Is a permanent user." + process_colors.get_colors())
    elif os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
        keep = input ("Are you going to keep this " + username+"'s files? [Y/n]: ")
        if keep=="Y" or keep=="y":
            os.remove("etc/users/"+username)
        elif keep=="N" or keep=="n" or keep=="\0":
            shutil.rmtree("desk/"+username,ignore_errors=False, onerror=None)
            os.remove("etc/users/"+username)
    else:
        print(process_colors.get_fail()   +username+ ": user not found." + process_colors.get_colors())
def passwd (username):
    if username=="root" and os.path.isdir("root") and os.path.isfile("etc/users/root"):
        shutil.copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
        switch_user = reload(switch_user)
        if switch_user.security == True:
            login = input("Enter " + username + "'s password: ")
            if login == switch_user.code:
                change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                if change_security == "Y" or change_security == "y":
                    security = input("Change user security [T/f]: ")
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("name = \"" + username + "\"\n")
                    if security == "T" or security == "t":
                        change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                        if change_password == "Y" or change_password == "y":
                            while True:
                                password = input("Set user a new password: ")
                                code = input("Confirm a new password: ")
                                if password == code:
                                    file.write("security = True\n")
                                    file.write("code = \"" + password + "\"")
                                    file.close()
                                    break
                                else:
                                    print(
                                        process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
                        elif change_password == "n" or change_password == "N":
                            file.write("security = True\n")
                            file.write("code = \"" + switch_user.code + "\"")
                            file.close()
                    elif security == "f" or security == "F" or security == "\0":
                        file.write("security = False\n")
                        file.close()
                elif change_security == "n" or change_security == "N" or  change_security == "\0":
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("security = " + str(switch_user.security) + "\n")
                    file.close()
            else:
                print(process_colors.get_fail()   + "Wrong password." + process_colors.get_colors())
        else:
            change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
            if change_security == "Y" or change_security == "y":
                security = input("Change user security [T/f]: ")
                file = open("etc/users/" + username + ".py", "a")
                file.write("name = \"" + username + "\"\n")
                if security == "T" or security == "t":
                    change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                    if change_password == "Y" or change_password == "y":
                        while True:
                            password = input("Set user a new password: ")
                            code = input("Confirm a new password: ")
                            if password == code:
                                file.write("security = True\n")
                                file.write("code = \"" + password + "\"")
                                file.close()
                                break
                            else:
                                print(process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
                    elif change_password == "n" or change_password == "N" or change_password == "\0":
                        file.write("security = True\n")
                        file.write("code = \"" + switch_user.code + "\"")
                        file.close()
                elif security == "f" or security == "F" or  security == "\0":
                    file.write("security = False\n")
                    file.close()
            elif change_security == "n" or  change_security == "N" or  change_security == "\0":
                file = open("etc/users/" + username + ".py", "a")
                file.write("security = " + str(switch_user.security) + "\n")
                file.close()

        src = "etc/users/" + username + ".py"
        dest = "etc/users/" + username
        if os.path.isfile(src):
            py_compile.compile(src, dest)
            os.remove(src)
    else:
        if os.path.isfile("etc/users/" + username) and os.path.isdir("desk/" + username):
            shutil.copyfile("etc/users/" + username, "var/switch_user.pyc")
            from var import switch_user
            if switch_user.security == True:
                login = input("Enter " + username + "'s password: ")
                if login == switch_user.code:
                    change_admin = input("Do you want to change " + username + "'s type? [Y/n]: ")
                    if change_admin == "Y" or change_admin == "y":
                        admin = input("Change user type [A/S]: ")
                        if admin == "A" or admin == "a":
                            file = open("etc/users/" + username + ".py", "w")
                            file.write("admin = True\n")
                            file.close()
                        elif admin == "S" or admin == "s":
                            file = open("etc/users/" + username + ".py", "w")
                            file.write("admin = False\n")
                            file.close()
                    elif change_admin == "n" or change_admin == "N" or change_admin == "\0":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = " + str(switch_user.admin) + "\n")
                        file.close()
                    change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                    if change_security == "Y" or change_security == "y":
                        security = input("Change user security [T/f]: ")
                        file = open("etc/users/" + username + ".py", "a")
                        file.write("name = \"" + username + "\"\n")
                        if security == "T" or security == "t":
                            change_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                            if change_password == "Y" or change_password == "y":
                                while True:
                                    password = input("Set user a new password: ")
                                    code = input("Confirm a new password: ")
                                    if password == code:
                                        file.write("security = True\n")
                                        file.write("code = \"" + password + "\"")
                                        file.close()
                                        break
                                    else:
                                        print(
                                            process_colors.get_fail() + "Wrong password! Try agian.\n" + process_colors.get_colors())
                            elif change_password == "n" or change_password == "N" or change_password == "\0":
                                file.write("security = True\n")
                                file.write("code = \"" + switch_user.code + "\"")
                                file.close()
                        elif security == "f" or security == "F" or security == "\0":
                            file.write("security = False\n")
                            file.close()
                    elif change_security == "n" or change_security == "N" or change_security == "\0":
                        file = open("etc/users/" + username + ".py", "a")
                        file.write("security = " + str(switch_user.security) + "\n")
                        file.close()
                else:
                    print(process_colors.get_fail()  + "Wrong password." +process_colors.get_colors())
            else:
                change_admin = input("Do you want to change " + username + "'s type? [Y/n]: ")
                if change_admin == "Y" or change_admin == "y":
                    admin = input("Change user type [A/S]: ")
                    if admin == "A" or  admin == "a":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = True\n")
                        file.close()
                    elif admin == "S" or admin == "s":
                        file = open("etc/users/" + username + ".py", "w")
                        file.write("admin = False\n")
                        file.close()
                elif change_admin == "n" or change_admin == "N" or change_admin == "\0":
                    file = open("etc/users/" + username + ".py", "w")
                    file.write("admin = " + str(switch_user.admin) + "\n")
                    file.close()
                change_security = input("Do you want to change " + username + "'s security? [Y/n]: ")
                if change_security == "Y" or change_security == "y":
                    security = input("Change user security [T/f]: ")
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("name = \"" + username + "\"\n")
                    if security == "T" or security == "t":
                        chnage_password = input("Do you want to change " + username + "'s password? [Y/n]: ")
                        if chnage_password == "Y" or chnage_password == "y":
                            while True:
                                password = input("Set user a new password: ")
                                code = input("Confirm a new password: ")
                                if password == code:
                                    file.write("security = True\n")
                                    file.write("code = \"" + password + "\"")
                                    file.close()
                                    break
                                else:
                                    print(process_colors.get_fail()   + "Wrong password! Try agian.\n" + process_colors.get_colors())
                        elif chnage_password == "n" or chnage_password == "N" or chnage_password == "\0":
                            file.write("security = True\n")
                            file.write("code = \"" + switch_user.code + "\"")
                            file.close()
                    elif security == "f" or security == "F" or security == "\0":
                        file.write("security = False\n")
                        file.close()
                elif change_security == "n" or change_security == "N" or change_security == "\0":
                    file = open("etc/users/" + username + ".py", "a")
                    file.write("security = " + str(switch_user.security) + "\n")
                    file.close()

            src = "etc/users/" + username + ".py"
            dest = "etc/users/" + username
            if os.path.isfile(src):
                py_compile.compile(src, dest)
                os.remove(src)
        else:
            print(process_colors.get_fail()   + username + ": user not found." + process_colors.get_colors())
def userinfo (username):
    if username=="root" and os.path.isdir ("root") and os.path.isfile ("etc/users/root"):
        copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + switch_user.name + process_colors.get_colors())
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "enable" +process_colors.get_colors())
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "disable" + process_colors.get_colors())
    elif os.path.isdir ("desk/"+username) and os.path.isfile("etc/users/"+username):
        copyfile("etc/users/" + username, "var/switch_user.pyc")
        from var import switch_user
        switch_user = reload(switch_user)
        print("    Username:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + switch_user.name +process_colors.get_colors())
        if switch_user.admin == True:
            print("    Type:       " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "Administrator" + process_colors.get_colors())
        else:
            print("    Type:       " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "Standard" + process_colors.get_colors())
        if switch_user.security == True:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "enable" +process_colors.get_colors())
        else:
            print("    Security:   " + process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "disable" + process_colors.get_colors())
    elif username=="" or username==" ":
        print()
    else:
        print(process_colors.get_fail()   +username+ ": user not found." +process_colors.get_colors())
def ls (path):
    if os.path.isdir (root+"/"+path):
        dirs = os.listdir(root + "/" + path)
        for dir in dirs:
            if os.path.isfile(root + "/" + path + "/" + dir):
                print(dir + process_colors.get_colors())
            else:
                print(process_colors.get_path() + dir + "/" + process_colors.get_colors())
    else:
        print(process_colors.get_fail()   +path+ ": directory not found." +process_colors.get_colors())
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
def exec (filename,args):
    if os.path.isfile( "bin/" + filename + ".pyc"):
        process.clean_switch()
        copyfile("bin/" + filename + ".pyc", "var/switch_process.pyc")
        from var import switch_process
        switch_process = reload(switch_process)
        switch_process.main(args)
        process.clean_switch()
def su (user_already,username):
    if user_already==username:
        print(process_colors.get_warning() +username+ ": user already switched." + process_colors.get_colors())
    else:
        if username=="root":
            enter_password("root","#")
        elif os.path.isdir ("desk/"+username) and os.path.isfile ("etc/users/"+username):
            enter_password(username,"$")
        else:
            print(process_colors.get_fail()  + username + ": user not found." + process_colors.get_colors())
def logout():
    k_login()
def reboot():
    import vmwet
    vmwet = reload(vmwet)
def userlist ():
    users = os.listdir("desk/")
    for user in users:
        if os.path.isfile ("etc/users/"+user):
            print (process_colors.color(1,process_colors.white,process_colors.get_bgcolor())+"\t"+user+process_colors.get_colors()+"\tActive")
        else:
            print (process_colors.get_fail()  +"\t"+user+process_colors.get_colors()+"\tInactive")
    print(process_colors.color(1,process_colors.white,process_colors.get_bgcolor()) + "\troot"+process_colors.get_colors()+ "\tActive")

root = "."
path = "/"

def k_init():
    print (" \n")
    process.show_power_on()
    process.show_start_process("init")

    if not os.path.isdir ("bin"): os.mkdir ("bin")
    if not os.path.isdir("desk"): os.mkdir("desk")
    if not os.path.isdir("root"): os.mkdir("root")
    if not os.path.isdir("var"): os.mkdir("var")
    if not os.path.isdir("var/shell"): os.mkdir("var/shell")

k_init()

def k_distro ():
    process.show_start_process("distro")

    py_compile.compile ("etc/distro","var/distro.pyc")

    from var import distro
    distro = reload(distro)

    print("\n"+"Welcome to "+distro.name+" "+distro.version+"\n")

k_distro()

def k_issue():
    process.show_start_process("issue")

    print()
    show_issue()
    print()

k_issue()
def process_shell():
    file = open ("etc/process","r")
    i = int(file.readline())
    file.close()
    while True:
        if not os.path.isdir("var/shell/"+str(i)):
            os.mkdir ("var/shell/"+str(i))
            file = open ("etc/process","w")
            file.write(str(i))
            file.close()
            break
        else:
            i = i + 1
            os.mkdir ("var/shell/"+str(i))
            file = open("etc/process", "w")
            file.write(str(i))
            file.close()
            break

def process_path ():
    file = open("etc/process", "r")
    i = file.readline()
    file.close()
    return "var/shell/"+i

def terminal(commandline,command,username,command_symbol,path):
    if command == "" or command == " " or command.startswith("#") or command.startswith("//") or (command.startswith("/*") and command.endswith("*/")):
        print(end='')
    elif command == "shut":
        print()
        shut()
    elif command == "ver":
        ver()
    elif commandline[0] == "out":
        out(commandline[1:])
    elif commandline[0] == "mkdir":
        mkdir(commandline[1:])
    elif commandline[0] == "rmdir":
        rmdir(commandline[1:])
    elif commandline[0] == "rm":
        rm(commandline[1:])
    elif commandline[0] == "cat":
        cat(commandline[1:])
    elif command == "help":
        help()
    elif commandline[0] == "cp":
        cp(commandline[1:])
    elif commandline[0] == "mv":
        mv(commandline[1:])
    elif commandline[0] == "useradd":
        useradd(commandline[1])
    elif commandline[0] == "userm":
        userm(commandline[1])
    elif commandline[0] == "passwd":
        passwd(commandline[1])
    elif command == "userinfo":
        userinfo(username)
    elif commandline[0] == "userinfo":
        userinfo(commandline[1])
    elif command == "ls":
        ls(path)
    elif commandline[0] == "ls":
        ls(commandline[1])
    elif commandline[0] == "su":
        su(username, commandline[1])
    elif command == "logout" or command == "exit":
        print()
        process.show_end_process("shell")
        logout()
    elif command == "reboot":
        print()
        process.show_end_process("shell")
        process.show_reboot()
        reboot()
    elif commandline[0] == "pyc":
        pyc(commandline[1:])
    elif command == "userlist":
        userlist()
    elif command == "license":
        license()
    elif commandline[0] == "pack":
        pack(commandline[1:])
    elif commandline[0] == "unpack":
        unpack(commandline[1:])
    elif os.path.isfile("bin/" + commandline[0] + ".pyc"):
        exec(commandline[0], commandline[1:])
    else:
        print(process_colors.get_fail()  + commandline[0] + ": command not found." + process_colors.get_colors())

def k_shell(username,command_symbol,path):
    process_shell()
    print()
    process.show_start_process("shell")
    print()
    while True:
        color_prompt =process_colors.get_colors()
        color_path =process_colors.get_colors()
        if username=="root":
            color_prompt = process_colors.get_colors()
            color_path = process_colors.get_colors()
        else:
            color_prompt = process_colors.get_prompt()
            color_path = process_colors.get_path()

        command = input (color_prompt+username+"@"+get_hostname()+process_colors.color(process_colors.get_style(),process_colors.white,process_colors.get_bgcolor())+":"+color_path+path+process_colors.get_colors()+ command_symbol+" ")
        commandline = command.split(" ")

        if commandline[0] == "cd":
            for i in commandline[1:]:
                if commandline[1]=="" or commandline[1]==" ":
                    path = ""
                elif commandline[1].startswith("/"):
                    if os.path.isdir(root + "/" + commandline[1]):
                        path = commandline[1]
                    else:
                        print(process_colors.get_fail()  + commandline[1] + ": directory not found." + process_colors.get_colors())
                else:
                    if os.path.isdir(root+"/"+path+"/"+commandline[1]):
                        if path == "/":
                            path = path + commandline[1]
                        else:
                            path = path + "/" + commandline[1]
                    else:
                        print(process_colors.get_fail()  + commandline[1] + ": directory not found." +process_colors.get_colors())
        else:
            terminal(commandline,command,username,command_symbol,path)

def k_login():
    process.show_start_process("login")

    while True:
        username = input ("\nEnter a username: ")
        if username=="root" and os.path.isdir ("root") and  os.path.isfile("etc/users/root"):
            enter_password("root","#")
        if os.path.isfile ("etc/users/"+username) and os.path.isdir ("desk/"+username):
            enter_password(username,"$")
        elif username=="" or username.startswith(" "):
            continue
        else:
            print (process_colors.get_fail() +username+": user not found."+process_colors.get_colors())

k_login()
