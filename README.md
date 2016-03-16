## Linux-Server-Application submission
Linux Server Configuration and Deployment of AdoptUsDogs

15/03/2016 Andrew Moore

These files highlight the sequences necessary for basic configuration, secure access, firewall implementation and final deployment of a previously developed catalog application, AdoptUsDogs, on a provided linux server environment.

Prior instructions for use of the application itself can be found here: [AdoptUsDogs](https://github.com/erooma/Catalog-Application).

Please note that this current rendering does NOT include all files sources. In particular, files and packages from the virtual environment on the linux server are not included in this repository.

Sources and information used for each step in this README file are included after each section.

### Basic Linux Configuration

####a. Launch the machine as provded per Udacity and remote login as root user.

####b. Create a new user *grader* with password.
 
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
 
####c. Update all packages using the following commands:

 >`sudo apt-get update`

 >`sudo apt-get upgrade`

Add packages that automatically monitor for updates:

>`sudo apt-get install unattended-upgrades`

>`sudo dpkg-reconfigure --priority=low unattended-upgrades`

Add a program that can be used to monitor your system in real time

>`sudo apt-get install python-pip build-essential python-dev`

>`sudo pip install Glances`

>`sudo pip install PySensors`


####d. Configure system to have a local timezone of UTC

>`tzconfig`

Server is presently set to UTC so no changes are necessary.

### Securing the server

####e. Change the SSH port from 22 to 2200. Ensure that SSH access via port 2200 is set in */etc/ssh/sshd_config*.

>`# What ports, IPs and protocols we listen for`

>`Port 2200`

(you may wish to have PasswordAccess while performing these operations in case there is a timing error!)

####f. Determine ufw (firewall) status with the following command:

>`ufw status`

Once determining that ufw is disabled, change the ports as required:

>`sudo ufw allow 2200/tcp` for ssh login

>`sudo ufw allow 80/tcp` for HTTP

>`sudo ufw allow 123/udp` for NTP

>`sudo ufw enable` to enable the firewall

####g. Consider addition of additional protection to monitor for repeated unsuccessful login attempts and ban attackers.

>`sudo apt-get install fail2ban`

>`sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local` to copy the local config file


Implement the following changes in the configuration file: 

```
set bantime  = 1800

destemail = admin@SERVER

action = %(action_mwl)s

change ssh port to = 2220
```

Then ensure that the service is running.

>`sudo service fail2ban stop`

>`sudo service fail2ban start`



This package can alert the administrator of necessary upgrades via email.

Install application *sendmail* (or other mail package) in anticipation of mail access.

note: email functionality has not been fully implemented on this server


### Installing the application

####h. Install and configure Apache to serve a Python mod_wsgi application

(i) Install Apache2 and components

>`sudo apt-get install apache2`

>`sudo apt-get install python-setuptools libapache2-mod-wsgi` to install wsgi module

>`sudo a2enmod wsgi` to enable wsgi module

>`sudo service apache2 restart` to restart after making (multiple) modifications

In order to remove error message "Could not reliably determine the servers's fully qualified domain name" create an empty Apache config file with the hostname:

>`echo "ServerName HOSTNAME"`

>`sudo tee /etc/apache2/conf-available/fqdn.conf`

>`sudo a2enconf fqdn` to enable new config file

(ii) Begin to prepare for serving a flask app (puppies) through apache2:

>`cd /var/www`

>`sudo mkdir puppies`

>`cd puppies`

>`sudo mkdir puppies`

>`cd puppies`

>`sudo mkdir static templates`


Create the starter python/flask file.

>`sudo nano __init__.py` which contains the following code.

```python
  from flask import Flask  
  app = Flask(__name__)  
  @app.route("/")  
  def hello():  
    return "Hello worlds"  
  if __name__ == "__main__":  
    app.run()  
```
 
(iii) Install Flask and create the virtual machine

Install pip for python

>`sudo apt-get install python-pip`

Prepare virtual environment (directory /var/www/puppies/puppies/venv/), and name it 'venv'.

>`sudo pip install virtualenv`

>`sudo virtualenv venv`

Enable all permissions from within venv and then activate it.

>`sudo chmod -R 777 venv`

>`source venv/bin/activate`

From within the virtual environment, install Flask.

>`pip install Flask`

Establish that the app is working (run \_\_init\_\_.py then deavtivate the environment)

>`python __init__.py`

>`deactivate`

(iv) Create and enable a new virtual host

Create a virtual host config file

>`sudo nano /etc/apache2/sites-available/puppies.conf`

Add the following lines of code using PUBLIC-IP-ADDRESS given by Udacity

```python
    <VirtualHost *:80>
      ServerName PUBLIC-IP-ADDRESS
      ServerAdmin admin@PUBLIC-IP-ADDRESS
      ServerAlias ec2-XX-XX-X-XX.us-west-2.compute.amazonaws.com    # necessary for certain oauth2 authentications/*/*
      WSGIScriptAlias / /var/www/puppies/puppies.wsgi
      <Directory /var/www/puppies/puppies/>
          Order allow,deny
          Allow from all
      </Directory>
      Alias /static /var/www/puppies/puppies/static
      <Directory /var/www/puppies/puppies/static/>
          Order allow,deny
          Allow from all
      </Directory>
      ErrorLog ${APACHE_LOG_DIR}/error.log
      LogLevel warn
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
 ```
  
Enable the virtual host:

>`sudo a2ensite puppies`

/*/* this line is necessary for oauth2 authentication. Replace X with appropriate server address.


(v) Create the wsgi file.

>`cd /var/www/puppies`

>`sudo vim puppies.wsgi`

Add the following code to puppies.wsgi
  
  ```python
  #!/usr/bin/python
  import sys
  import logging
  logging.basicConfig(stream=sys.stderr)
  sys.path.insert(0,"/var/www/puppies/")

  from puppies import app as application
  application.secret_key = 'Add your secret key'
  ```
  
Restart Apache.

>`sudo service apache2 restart`


(vi) Install additional python modules to be required by the app puppies

>`source venv/bin/activate` activate virtual environment

>`pip install httplib2` install httplib2 module

>`pip install requests` install requests module

>`pip install flask_wtf`

>`pip install wtforms`

>`pip install sqlalchemy`

>`pip install httplib2`

>`pip install werkzeug`

>`pip install oauth2client`

>`sudo apt-get install python-psycopg2` install the Python PostgreSQL adapter psycopg


####i. Install and configure PostgreSQL

 (i) Installation
 
 >`sudo apt-get install postgresql postgresql-contrib`
 
 Ensure that no remote connections are allowed by examining the pga-hba config file
 
 >`sudo nano /etc/postgresql/931/main/pg_hba.conf`
 
 
 (ii) Create a new user named catalog that has limited permissions to your catalog application database
 
Create Linux user *catalog* (will not have remote access via keys)
 
 >`sudo adduser catalog` 

Enter database server as postgres user and create new user named *catalog*

>`sudo -i -u postgres`

>`psql` to enter

>`CREATE USER catalog WITH PASSWORD 'xxxxxx';` choosing a password for user catalog

>`ALTER USER catalog CREATEDB;` allowing user catalog privileges to create databases
 
>`CREATE DATABASE puppyshelter WITH OWNER catalog;` allowing user catalog ownership of application database
 
 
####j. Install git and setup the AdoptUsDogs application

(i) Install git

>`sudo apt-get install git`

(ii) Clone catalog application to the linux server and copy files into puppies directory on server

>`git clone https://github.com/erooma/Catalog-Application.git`

(iii) Render .git directory inaccessible

Create an *.htaccess* file with the following code `RedirectMatch 404 /\.git`

(iv) Modify app files and settings

Ensure that *runserver.py* file becomes working *puppies.wsgi* in addition to */puppies/\_\_init.py\_\_* file

(v) Ensure functional third-party authentication

Modify Google developer's console to include full web address (eg: ec2-XX-XX-X-XX.us-west-2.compute.amazonaws.com) rather than public server under *Authorized Redirect URI's* in addition to both public IP address and full web address under *Javascript Origins*

Full login functions when deploying the application required changes to code include jsonification of credentials information

```python
    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.to_json()
    login_session['gplus_id'] = gplus_id
 ```
 
 And as a consequence, loading as json when revoking the access token from logged in user

```python
    # Execute HTTP GET request to revoke current token.
    access_token = json.loads(credentials)['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
 ```

### Known issues

The use of Postgresql has a known issue - inability to have a table named *User* without expressly using quotation marks at every occurrence. The AdoptUsDogs application was therefore re-coded to implement a table *Client* instead of User when manipulating data.


This application is coded in python and uses the frAdd postgre user with password:
Sources: Trackets Blog and Super Useameworks Flask, 
http://flask.pocoo.org/, and the extensions FlaskWTF, 
https://flask-wtf.readthedocs.org/en/latest/, and WTForms, 
https://wtforms.readthedocs.org/en/latest/.

HTML templating uses jquery and bootstrap frameworks.
