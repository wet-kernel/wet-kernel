# Wet kernel

This kernel written with Python programing language that you can run it on computer or other device (e.g. on cloud drives).

For build this kernel you should do:

1- Get Wet kernel with this command:

`git clone https://github.com/wet-kernel/wet`

2- Build the kernel:

`cd ~/wet`

`make all`

3- Copy kernel's directory:

`cp -rv stor/* [another directory]`

for example:

`cp -rv stor/* ~/Dropbox/wet`

4- Run the kernel

`cd [kernel's directory]`

`python3 vmwet.pyc`

for example:

`cd ~/Dropbox/wet`

`python3 vmwet.pyc`

Than login with root user account, for see commands run `help` command in kernel's shell.

 # Screenshot from Wet kernel:
![](https://github.com/wet-kernel/wet/blob/master/screenshot.png)


Created by Editor.md
