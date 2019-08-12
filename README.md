# Wet kernel

This kernel written with Python programing language that you can run it on computer or other device (e.g. on cloud drives).

For build this kernel you should do:

1- Get Wet kernel with this command:

`git clone https://github.com/wet-kernel/wet`

2- Build the kernel:

`cd ~/wet`
`make all`

3- Run the kernel

`make run`
or
`cd stor && python3 vmwet.pyc`
 # Screenshot from Wet kernel:
![](https://github.com/wet-kernel/wet/blob/master/Screenshot%20from%202019-08-12%2014-26-08.png)

# Login on kernel:

First run the kernel than login with root user
Try help for see commands

# Create an user on Wet kernel:

1. Run `useradd example` on Wet terminal.
2. Choose your user type (A: Admin, S: Standard).
3. Choose your security (T: true, f: False)
If you choose (T) for security you should enter a new password for your user.
4. For create this user enter 'Y'.

If you want to edit your user run `passwd example`

If you want to delete your user run `userm example`

Switch an user: Run `su example`

List users on terminal: Run `userlist`

See user information: Run `userinfo example`

# End
