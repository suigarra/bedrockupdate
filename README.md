# bedrockupdate
a bash script for updating bedrock and all stratums
# installation
packages needed = bash & sudo

download the bash script and move it into /bedrock/bin/:

         sudo cp /path/to/bedrockupdate /bedrock/bin/
         
now make sure to change the permissions of the bash script so we can execute it

         sudo chmod +x /bedrock/bin/bedrockupdate
         
done, now u can test bedrockupdate:

         bedrockupdate
         
# add new stratums to the script
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

replace "stratumname" with the stratums name and stratumupdate with the stratum's package manager command that updates it

   
