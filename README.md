# bedrockupdate
a simple bash script for updating bedrock and all stratums

<img src="https://img.shields.io/badge/-BedrockLinux_0.7-blue?style=social&logo=linux&logoColor=black"> <img src="https://img.shields.io/badge/-GNU_Bash-white?style=social&logo=gnu%20bash&logoColor=black">

# installation
packages needed = <ins>bash, python & sudo</ins>



run **install.sh** (u must chmod +x the file before):

     ./install.sh

# add new stratums to the script
the script only has main stratums, so if u need to add one
heres a template to add new stratums to script:

   ```ruby
   if [ -d /bedrock/strata/stratumname ]; then
      echo "Found stratumname Stratum !"
      echo "Running Updates.."
      sudo brl strat stratumname stratumupdate
      echo "stratumname Done !"
      number=$((number+1))
   fi
   ```

file is at **/bedrock/bin/bedrockupdate**

replace **"stratumname"** with the stratums name 
and **"stratumupdate"** with the stratum's package manager command that updates it

   
