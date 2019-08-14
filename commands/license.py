def license ():
    file = open ("etc/license","r")
    strv = file.read()
    file.close()
    print (strv)