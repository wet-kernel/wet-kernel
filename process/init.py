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