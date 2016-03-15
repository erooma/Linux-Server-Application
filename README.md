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

Then place the public key on the linux server under ~/.ssh as file *authorized_keys*.
Reset ssh access using the following:

 >`sudo service ssh restart`

Subsequent access is by private/public key access only including a passphrase for added security.
Disable password access for ALL accounts by changing the /etc/ssh/sshd_config file to the following:

 >`PasswordAuthentication no`
 
c. Update all packages using the following commands:

 >`sudo apt-get update`

 >`sudo apt-get upgrade`

Add packages that automatically monitor for updates:

>`sudo apt-get install unattended-upgrades`

>`sudo dpkg-reconfigure --priority=low unattended-upgrades`

These packages can alert the administrator of necessary upgrades via email.
Install application *sendmail* in anticipation of mail access via server.
(note: email functionality has not been fully implemented on this server)

d. Configure system to have a local timezone of UTC

>`tzconfig`

Server is presently set to UTC so no changes are necessary.

### Securing the server


e. Change the SSH port from 22 to 2200

f. Configure the Uncomplicated Firewall (UFW) to only allow incoming connections
for SSH (port 2200), HTTP (port 80), and NTP (port 123)


### Install the application

g. Install and configure Apache to serve a Python mod_wsgi application

h. Install and configure PostgreSQL:
   i. Do not allow remote connections
   ii. Create a new user named catalog that has limited permissions to your catalog application database
   
i. Install git, clone and set up your Catalog App project (from your GitHub
repository from earlier in the Nanodegree program) so that it functions correctly
when visiting your server’s IP address in a browser. Remember to set this up
appropriately so that your .git directory is not publicly accessible via a browser!

j. Reconfiguration of third-party authentication (eg: changes on Google Developer's Console to reflect 

### Additional features

The following features have been added to enhance security and functionality.
1.
2.


### Known issues

The use of Postgresql has a known issue - inability to have a table named *User* without expressly using quotation marks at every occurrence. The AdoptUsDogs application was therefore re-coded to implement a table *Client* instead of User when manipulating data.


This application is coded in python and uses the frameworks Flask, 
http://flask.pocoo.org/, and the extensions FlaskWTF, 
https://flask-wtf.readthedocs.org/en/latest/, and WTForms, 
https://wtforms.readthedocs.org/en/latest/.

HTML templating uses jquery and bootstrap frameworks.
