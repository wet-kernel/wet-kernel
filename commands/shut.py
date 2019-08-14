
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