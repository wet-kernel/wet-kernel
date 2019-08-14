def exec (filename,args):
    if os.path.isfile( "bin/" + filename + ".pyc"):
        process.clean_switch()
        copyfile("bin/" + filename + ".pyc", "var/switch_process.pyc")
        from var import switch_process
        switch_process = reload(switch_process)
        switch_process.main(args)
        process.clean_switch()