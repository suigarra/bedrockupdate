# bedrockupdate
a bash script for updating bedrock and all stratums
# installation
packages needed = bash & sudo

download the bash script and make a PATH for it:
         mkdir ~/.bash_scripts
move the bash script inside of the PATH and add the following line to ~/.bashrc :
         export PATH:$PATH:~/.bash_scripts
update the ~/.bashrc by running:
         source ~/.bashrc
now make sure to change the permissions of the bash script so we can execute it
         chmod +x ~/.bash_scripts/bedrockupdate
done, now u can test bedrockupdate:
         bedrockupdate
