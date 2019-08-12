
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
            print (process_colors.FAIL+username+": user not found."+process_colors.ENDC)

k_login()