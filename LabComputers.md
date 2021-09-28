# Art Intel Computers

### Access Information
<!-- $$$ Brightspace update each semester -->
The login information is linked on the course page on [Brightspace Lab Computer Logins](https://brightspace.nyu.edu/d2l/le/lessons/110671/units/5937697)

You can connect with TeamViewer to the Linux desktop, or connect using ssh (while on the NYUAD network or using NYUAD VPN). Physical access is not currently allowed.

# Linux / Python
Here are some tutorials to get you started with the command line and Python

1. Linux command-line (basically the same as OSX command line)

https://ubuntu.com/tutorials/command-line-for-beginners#1-overview

2. Python tutorial

https://www.programiz.com/python-programming/tutorial

### Setup
<!--
We'll be using Anaconda to manage our dependencies. I've set up CUDA and Tensorflow already and made a base conda environment for you to build off of. You need to clone this environment into your own personal environment:
- `conda create --name <YOURNAME> --clone tensorflow`
-->

We share the same Linux user account. Create your own subdirectory to hold all your files.
- `mkdir ~/<YOURNAME>`

Change into your directory after logging in.
- `cd <YOURNAME>`

We'll be using Anaconda to manage our dependencies. Anaconda allows us to create
a Python environment where we can install specific libraries, etc without disturbing
the rest of the system. Create your conda environment:
- `conda create --name <YOURNAME> --clone tensorflow-gpu`

Activate your conda environment.
- `conda activate <YOURNAME>`

**Each time you log in make sure to change into your user directory and activate your conda
environment. You should see the name of your conda environment at the beginning of the
command prompt.**

Any changes to Python version, python libraries, etc. you want to make will happen in your own environment.

**Please do NOT make changes to the system (e.g. using sudo) without asking Mang first.** If you activate your conda environment you should be able to do everything without using sudo.


### SSH
You can log into your assigned class computer remotely via SSH:
- `ssh nyuad@<IPADDRESS>`

<!--
### TMUX
We will use tmux for a detachable command line window. tmux commands:
- Check if there is another session running (list sessions): `tmux ls`
- Start a new session: `tmux new -s <YOURNAME>`
- Detach window (while in a session): `ctrl+b` then `d`
- Reattach to a session: `tmux a -t <NAMEOFSESSION>`
- Kill a session: `tmux kill-session -t <NAMEOFSESSION>`
-->

### Conda Usage
- activate env: `conda activate <YOUR_ENV_NAME>`
- deactivate env: `conda deactivate`
- list enviroments: `conda env list`
- remove an environment: `conda remove --name <YOUR_ENV_NAME> --all`

### Persistent terminal connections

You can use tmux to make a persistent terminal for running long scripts. The scripts
will keep running even if you disconnect (e.g. your wifi cuts out).

- [tmux: The 10 Most Important Commands](https://danielmiessler.com/study/tmux/)
- [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com/)

### SFTP
We'll use SFTP to move files between our computers and the class computers.

You can use the `sftp` command line program or GUI programs like Cyberduck.

sftp command line:
- SFTP into the class computer: `sftp nyuad@<IPADDRESS>`
- Normal unix file structure navigation commands work, but through the file structure on the class computer computer: `cd ls pwd`
- To navigate the file structure on your computer put an l before the commands for local: `lcd lls lpwd`
- Get a file from the class computer: `get <FILENAME>`
- Put a file from your computer on to the class computer: `put <FILENAME>`
- Get all files and folders in a directory: `get -r *`
- Quit SFTP: `bye`

Cyberduck SFTP:
- Download [Cyberduck](https://cyberduck.io/download/)
- If not on campus, connect to NYUAD VPN
- Click "Open Connection"
- Choose SFTP (SSH File Transfer Prototocol)
- Enter the server name (e.g. c3-129-lnx-01.abudhabi.nyu.edu)
- Enter user name (nyuad)
- Enter nyuad user password (linked from NYU Classes)
- Click Connect
- Drag and drop files to transfer
- If you create a new file on the Linux machine you have to hit Refresh in Cyberduck for it to be seen

![Cyberduck SFTP login](Assets/Cyberduck.png?raw=true "Cyberduck SFTP login")


### Misc.
- Remove a file: `rm <FILENAME>`
- Remove a folder with files in it: `rm -r <FOLDERNAME>` (Be careful with this command! Only in your directory.)
- Remove all files of a certain type (jpg in this example): `~rm *jpg`
- Check if other people are using the GPU `nvidia-smi`

### Locking the computers
When working on the actual computers **don't suspend** them when you're done. This will make it so no one can SSH into them. ***Lock them.***

### Fairplay
We have three computers for machine learning use. We need to share these three amongst all of us. So here are a few community rules:
- Only use these computers for dedicated machine learning tasks.
- Don't leave finished tasks still running on tmux.
- Move any output files you want to save to your computer and **delete all other generated files** as soon as a task is done.
- Each person will have one computer they are assigned to use. Please only use the computer you've been assigned to. If that computer is tied up for long periods, but another is free, let me know and we can talk about using a different computer.
- **Only add or change dependencies on your own environment**.
<!--
- Check to see if anyone is currently using the computer by checking the tmux sessions.
- Run ALL of your processes in tmux.
-->

### Lab Computers:
1: (AI1)

Name: c3-129-lnx-01.abudhabi.nyu.edu

IP address: 10.224.18.84


2: (AI2)

Name: c3-129-lnx-02.abudhabi.nyu.edu

IP address: 10.224.18.85


3: (AI3)

Name: c3-129-lnx-03.abudhabi.nyu.edu

IP address: 10.224.18.86


### VPN Login
See [instructions](https://www.nyu.edu/life/information-technology/getting-started/network-and-connectivity/vpn.html)

Enter 'push' as the secondary password to trigger 2FA.

![VPN login](Assets/VPN_login.png?raw=true "VPN login")


<!--
### Machine setup

wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

conda create -n tensorflow-gpu tensorflow-gpu

-->
