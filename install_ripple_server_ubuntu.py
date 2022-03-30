import subprocess as sp
import os
update_check = "sudo apt -y update"

install_utilities = "sudo apt -y install apt-transport-https ca-certificates wget gnupg"

trusted_key =  "wget -q -O - "+"https://repos.ripple.com/repos/api/gpg/key/public"+" | \
  sudo apt-key add -"

check_fingerp = "apt-key finger"

adding_resp_on_machine = "echo"+ "deb https://repos.ripple.com/repos/rippled-deb focal stable" +" | \
    sudo tee -a /etc/apt/sources.list.d/ripple.list"

update_ripple_resp = "sudo apt -y update"

install_ripple_software = "sudo apt -y install rippled"

check_ripple_status = "systemctl status rippled.service"

boot_auto = "sudo systemctl enable rippled.service"

commands  = [update_check,install_utilities,trusted_key,check_fingerp,adding_resp_on_machine,update_ripple_resp,install_ripple_software,
boot_auto]

command_len = len(commands)

for i in range(command_len):
	#check ripple status has been removed because it stops the installation
	os.system(commands[i])
