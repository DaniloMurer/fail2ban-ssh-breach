# Fail2Ban-SSH-Breach

Python script to breach into an Fail2Ban secured server via ssh.

## Strategy to brach the server

Fail2Ban can recognize attempted SSH braches and consequently bans the IP-Address of the attacker.
To bypass this system the script will try to connect to the target server via SSH, after every connection the script will change it's IP with Tor and STEM.

