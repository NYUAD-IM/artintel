# Art Intel Computers

### Setup
<!--
We'll be using Anaconda to manage our dependencies. I've set up CUDA and Tensorflow already and made a base conda environment for you to build off of. You need to clone this environment into your own personal environment:
- `conda create --name <YOURNAME> --clone tensorflow`
-->

We'll be using Anaconda to manage our dependencies. Anaconda allows us to create
a Python environment where we can install specific libraries, etc without disturbing
the rest of the system.
- `conda create --name <YOURNAME>`

Any changes to Python version, python libraries, etc. you want to make will happen in your own environment.

We share the same Linux user account. Create your own subdirectory to hold all your files.
- `mkdir ~/<YOURNAME>`

Change into your directory after logging in.
- `cd <YOURNAME>`

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
- activate env: `source activate <YOUR_ENV_NAME>`
- deactivate env: `source deactivate`
- list enviroments: `conda env list`
- remove an environment: `conda remove --name <YOUR_ENV_NAME> --all`

### SFTP
We'll use SFTP to move files between our computers and the class computers.

You can use the `sftp` command line program or GUI programs like Cyberduck.

- SFTP into the class computer: `sftp nyuad@<IPADDRESS>`
- Normal unix file structure navigation commands work, but through the file structure on the class computer computer: `cd ls pwd`
- To navigate the file structure on your computer put an l before the commands for local: `lcd lls lpwd`
- Get a file from the class computer: `get <FILENAME>`
- Put a file from your computer on to the class computer: `put <FILENAME>`
- Get all files and folders in a directory: `get -r *`
- Quit SFTP: `bye`

### Misc.
- The IP Address may change from time to time. While at the actual class computer get the ip address: `ifconfig`
- Remove a file: `rm <FILENAME>`
- Remove a folder with files in it: `rm -r <FOLDERNAME>` (Be careful with this command! Only in your directory.)
- Remove all files of a certain type (jpg in this example): `~rm *jpg`

### Locking the computers
When working on the actual computers **don't suspend** them when you're done. This will make it so no one can SSH into them. ***Lock them.***

### Fairplay
We have three computers for machine learning use. We need to share these three amongst all of us. So here are a few community rules:
- Only use these computers for dedicated machine learning tasks.
- Don't leave finished tasks still running on tmux.
- Move any output files you want to save to your computer and **delete all other generated files** as soon as a task is done.
- Each person will have one computer they are assigned to use. Please only use the computer you've been assigned to. If that computer is tied up for long periods, but another is free, let me know and we can talk about using a different computer.
- **Only add or change dependencies on your own environment**.
- Check to see if anyone is currently using the computer by checking the tmux sessions.
- Run ALL of your processes in tmux.

### Assigned Computers:
1: (AI)


2: (AI2)


3: (AI3)
