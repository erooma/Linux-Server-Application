## Linux-Server-Application submission
Linux Server Configuration and Deployment of AdoptUsDogs

15/03/2016 Andrew Moore

These files highlight the sequences necessary for basic configuration, secure access, firewall implementation and final deployment of a previously developed catalog application, AdoptUsDogs, on a provided linux server environment.

Prior instructions for use of the application itself can be found here: [AdoptUsDogs](https://github.com/erooma/Catalog-Application).

Please note that this current rendering does NOT include all files sources. In particular, files and packages from the virtual environment on the linux server are not included in this repository.

Sources and information used for each step in this README file are included after each section.

### Basic Linux Configuration

a. Launch the machine as provded per Udacity and remote login as root user.

b. Create a new user *grader* with password.
 
 >`adduser grader`
 
Add grader as a SUDOER user by adding a file *grader* within the directory /etc/sudoers.d.
   
 >`touch grader`
 
Generate new public and private keys for user *grader* remotely using command:
 >`ssh keygen`

Then place the public key on the linux server under (grader-home) ~/.ssh as file *authorized_keys*.

Modify Read/Write permissions as per user *grader* only.
Reset ssh access using the following:

 >`sudo service ssh restart`

Subsequent access is by private/public key access only including a passphrase for added security.

Disable password access for ALL accounts by changing the /etc/ssh/sshd_config file as follows:

 >`PasswordAuthentication no`
 
c. Update all packages using the following commands:

 >`sudo apt-get update`

 >`sudo apt-get upgrade`

Add packages that automatically monitor for updates:

>`sudo apt-get install unattended-upgrades`

>`sudo dpkg-reconfigure --priority=low unattended-upgrades`


d. Configure system to have a local timezone of UTC

>`tzconfig`

Server is presently set to UTC so no changes are necessary.

### Securing the server

e. Change the SSH port from 22 to 2200. Ensure that SSH access via port 2200 is set in */etc/ssh/sshd_config*.

>`# What ports, IPs and protocols we listen for`

>`Port 2200`

(you may wish to have PasswordAccess while performing these operations in case there is a timing error!)

f. Determine ufw (firewall) status with the following command:

>`ufw status`

Once determining that ufw is disabled, change the ports as required:

>`sudo ufw allow 2200/tcp` for ssh login

>`sudo ufw allow 80/tcp` for HTTP

>`sudo ufw allow 123/udp` for NTP

>`sudo ufw enable` to enable the firewall

g. Consider addition of additional protection to monitor for repeated unsuccessful login attempts and ban attackers.

>`sudo apt-get install fail2ban`

>`sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local` to copy the local config file

>`set bantime  = 1800`

  `destemail = admin@SERVER` 
  
  `action = %(action_mwl)s`
  
 `change ssh port to = 2220` 
  
>`sudo service fail2ban stop`

>`sudo service fail2ban start`


This package can alert the administrator of necessary upgrades via email.

Install application *sendmail* (or other mail package) in anticipation of mail access.

note: email functionality has not been fully implemented on this server

### Installing the application

h. Install and configure Apache to serve a Python mod_wsgi application

i. Install and configure PostgreSQL:
   i. Do not allow remote connections
   ii. Create a new user named catalog that has limited permissions to your catalog application database
   
j. Install git, clone and set up your Catalog App project (from your GitHub
repository from earlier in the Nanodegree program) so that it functions correctly
when visiting your server’s IP address in a browser. Remember to set this up
appropriately so that your .git directory is not publicly accessible via a browser!

k. Reconfiguration of third-party authentication (eg: changes on Google Developer's Console to reflect 

### Additional features

The following features have been added to enhance security and functionality.

1.
2.
3.



### Known issues

The use of Postgresql has a known issue - inability to have a table named *User* without expressly using quotation marks at every occurrence. The AdoptUsDogs application was therefore re-coded to implement a table *Client* instead of User when manipulating data.


This application is coded in python and uses the frameworks Flask, 
http://flask.pocoo.org/, and the extensions FlaskWTF, 
https://flask-wtf.readthedocs.org/en/latest/, and WTForms, 
https://wtforms.readthedocs.org/en/latest/.

HTML templating uses jquery and bootstrap frameworks.
