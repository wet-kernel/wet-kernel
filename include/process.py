class process:
    def show_start_process(process_name):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Start " + process_name + " process ...")

    def show_fail_process(process_name):
        print("[" + process_colors.get_fail()   + " Fail " +process_colors.get_colors() + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] End " + process_name + " process ...")

    def show_power_on ():
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.get_fail()   + " STOP " +process_colors.get_colors() + "] Stop the kernel ...")

    def show_power_off ():
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power off the kernel ...")

    def show_reboot():
        print("[" + process_colors.get_ok() + " OK " +process_colors.get_colors() + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Clean switch "+switch+" ...")

    def clean_switch():
        if os.path.isfile ("var/switch_process.pyc"):
            os.remove ("var/switch_process.pyc")
        if os.path.isfile ("var/switch_user.pyc"):
            os.remove ("var/switch_user.pyc")