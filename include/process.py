class process:
    def show_start_process(process_name):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Start " + process_name + " process ...")

    def show_fail_process(process_name):
        print("[" + process_colors.FAIL + " Fail " + process_colors.ENDC + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] End " + process_name + " process ...")

    def show_power_on ():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.FAIL + " STOP " + process_colors.ENDC + "] Stop the kernel ...")

    def show_power_off ():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Power off the kernel ...")

    def show_reboot():
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        print("[" + process_colors.OKGREEN + " OK " + process_colors.ENDC + "] Clean switch "+switch+" ...")

    def clean_switch():
        if os.path.isfile ("var/switch_process.pyc"):
            os.remove ("var/switch_process.pyc")
        if os.path.isfile ("etc/switch_user.pyc"):
            os.remove ("etc/switch_user.pyc")