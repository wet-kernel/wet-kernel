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