# bedrockupdate
a simple bash script for updating bedrock and all stratums

# installation
packages needed = <ins>bash, python & sudo</ins>



run **install.sh** (u must chmod +x the file before):

     ./install.sh

done, now u can run it by running:

     bedrockupdate

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

   
