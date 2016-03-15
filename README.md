## Linux-Server-Application submission
Linux Server Configuration and Deployment of AdoptUsDogs

15/03/2016 Andrew Moore

These files highlight the sequences necessary for basic configuration, secure access, firewall implementation and final deployment of a previously developed catalog application, AdoptUsDogs, on a provided linux server environment.

Prior instructions for use of the application itself can be found here: [AdoptUsDogs](https://github.com/erooma/Catalog-Application).

Please note that this current rendering does NOT include all files sources. In particular, files and packages from the virtual environment on the linux server are not included in this repository.

Sources and information used for each step in this README file are included after each section.

### Initial Linux Configuration

Without signing in, users will be able to see all of the puppies that are 
available for adoption, but only by signing in (through Google) are they
allowed to add puppies, adopt puppies, or edit or remove puppies that they
originally placed into the shelters. Users cannot edit or remove puppies 
that did not originally belong to them. Users can also see a list of puppies
that they adopted - these puppies are essentially removed from all shelters
but their records continue to exist in the database.

The information that can be added for a puppy includes its name, gender,
date of birth, weight (in lbs), special needs and a single image or photo 
(maximum 2 Mbytes) of the puppy in question (this is not obligatory).

### Mid-level operations

Users with more advanced admin privileges have the ability to edit, remove and
transfer all puppies from within the shelters. These users are also allowed to
edit shelter information (address, website, capacity, etc) or add new shelters.
Shelters cannot be filled beyond capacity.

### Highest level users

Users with the highest administration privilegs can see a list of all users in
the system in addition to their adopted puppies.

Choices from all  menus will change depending on the user privileges.

The presence of a *demonstration* option on the main screen
for a user to temporarily change his/her administrator privileges. 
This is for evaluation purposes only, and allows the evaluator to see the 
changes available at each administration level.

### Data options

Within the drop down menus are choices for the user to download data of
either shelters, or puppies within a selected shelter, by means of JSON or
XML coding.

### Known issues

Please note that full user administration (deletion, password reminders etc)
has not been implemented in this version, in part because of the use of the
OAuth2 Google log-in.

This version contains demonstration puppies with images, shelters and
users for evaluation purposes. No similarities with real shelters, dogs, or 
users is implied or intended. All images have been obtained royalty-free.

### Requirements

The application is run from the file: runserver.py and uses localhost: 5000 on
a virtual server.

The client_secrets file from Google developers console has not been included
for security purposes.

This application is coded in python and uses the frameworks Flask, 
http://flask.pocoo.org/, and the extensions FlaskWTF, 
https://flask-wtf.readthedocs.org/en/latest/, and WTForms, 
https://wtforms.readthedocs.org/en/latest/.

HTML templating uses jquery and bootstrap frameworks.
