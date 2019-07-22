# Using Cert with ACI and Ansible


### To Use

Create Cert and key for ansible. See this [link](https://docs.ansible.com/ansible/latest/scenario_guides/guide_aci.html) for more information.


`openssl req -new -newkey rsa:1024 -days 36500 -nodes -x509 -keyout admin.key -out admin.crt -subj '/CN=Admin/O=Your Company/C=US'`

Configure your local user, Perform the following steps:

* Add the X.509 certificate to your ACI AAA local user at ADMIN » AAA
* Click AAA Authentication
* Check that in the Authentication field the Realm field displays Local
* Expand Security Management » Local Users
* Click the name of the user you want to add a certificate to, in the User Certificates area
* Click the + sign and in the Create X509 Certificate enter a certificate name in the Name field
	* If you use the basename of your private key here, you don’t need to enter certificate_name in Ansible
* Copy and paste your X.509 certificate in the Data field.





