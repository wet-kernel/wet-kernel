import py_compile, os

def kernel_header():
    file = open ("kernel_header.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/kernel_header","w")
    file.close()

def imports():
    file = open ("imports.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/imports","w")
    file.close()

def lib_process():
    file1 = open ("include/process_colors.py","r")
    strv1 = file1.read()
    file1.close()
    file2 = open("include/process.py", "r")
    strv2 = file2.read()
    file2.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv1+"\n")
    vmwet_file.write(strv2+"\n")
    vmwet_file.close()
    file = open("jobs/lib_process","w")
    file.close()
def lib_issue():
    file = open ("include/issue.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/lib_issue","w")
    file.close()

def lib_hostname():
    file = open ("include/hostname.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/lib_hostname","w")
    file.close()

def lib_user():
    file = open ("include/user.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/lib_user","w")
    file.close()

def lib_permissions():
    file = open ("include/permissions.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/lib_permissions","w")
    file.close()


# Command unit

def commands():
    file = open ("commands.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/commands","w")
    file.close()

# Process units

def process_init():
    file = open ("process/init.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/process_init","w")
    file.close()

def process_distro():
    file = open ("process/distro.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/process_distro","w")
    file.close()

def process_issue():
    file = open ("process/issue.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/process_issue","w")
    file.close()

def process_shell():
    file = open ("process/shell.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/process_shell","w")
    file.close()

def process_login():
    file = open ("process/login.py","r")
    strv = file.read()
    file.close()
    vmwet_file = open("init.py","a")
    vmwet_file.write(strv+"\n")
    vmwet_file.close()
    file = open("jobs/process_login","w")
    file.close()

def compile():
    py_compile.compile("init.py","stor/vmwet.pyc")

if not os.path.isfile("jobs/kernel_header"):
    kernel_header()
if not os.path.isfile("jobs/imports"):
    imports()
if not os.path.isfile("jobs/lib_process"):
    lib_process()
if not os.path.isfile("jobs/lib_issue"):
    lib_issue()
if not os.path.isfile("jobs/lib_hostname"):
    lib_hostname()
if not os.path.isfile("jobs/lib_user"):
    lib_user()
if not os.path.isfile("jobs/lib_permissions"):
    lib_permissions()
if not os.path.isfile("jobs/commands"):
    commands()
if not os.path.isfile("jobs/process_init"):
    process_init()
if not os.path.isfile("jobs/process_distro"):
    process_distro()
if not os.path.isfile("jobs/process_issue"):
    process_issue()
if not os.path.isfile("jobs/process_shell"):
    process_shell()
if not os.path.isfile("jobs/process_login"):
    process_login()
compile()