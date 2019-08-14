
def k_distro ():
    process.show_start_process("distro")

    py_compile.compile ("etc/distro","var/distro.pyc")

    from var import distro
    distro = reload(distro)

    print("\n"+"Welcome to "+distro.name+" "+distro.version+"\n")

k_distro()