def get_hostname():
    hostname_filename = "etc/hostname"
    file = open (hostname_filename,"r")
    strv = file.readline()
    file.close()
    return strv
