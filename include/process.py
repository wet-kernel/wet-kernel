class process:
    def show_start_process(process_name):
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " + process_colors.color(0,process_colors.white,40) + "] Start " + process_name + " process ...")

    def show_fail_process(process_name):
        print("[" + process_colors.color(0,process_colors.red,40)  + " Fail " + process_colors.color(0,process_colors.white,40) + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " + process_colors.color(0,process_colors.white,40) + "] End " + process_name + " process ...")

    def show_power_on ():
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " + process_colors.color(0,process_colors.white,40) + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.color(0,process_colors.red,40)  + " STOP " + process_colors.color(0,process_colors.white,40) + "] Stop the kernel ...")

    def show_power_off ():
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " + process_colors.color(0,process_colors.white,40) + "] Power off the kernel ...")

    def show_reboot():
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " +process_colors.color(0,process_colors.white,40) + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        print("[" + process_colors.color(0,process_colors.green,40) + " OK " + process_colors.color(0,process_colors.white,40) + "] Clean switch "+switch+" ...")

    def clean_switch():
        if os.path.isfile ("var/switch_process.pyc"):
            os.remove ("var/switch_process.pyc")
        if os.path.isfile ("etc/switch_user.pyc"):
            os.remove ("etc/switch_user.pyc")