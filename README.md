# ACI Automation Demos

This is a repository to consolidate my ACI demos. This is a mash up of content I found as well as my own content. Details can be found within each section.

- Terraform
- Curling
- Ansible
- Postman
- UCS Director (coming soon...)

I recommend runing a vritualenv environment for these with Python 3. By design, I tried to keep the ansible configs local to the virtualenv. So you'll need to edit the ansible.cfg file to point to your interpeter. You'll find the ansible.cfg file within various folders.

Here's an example of the config:

			# config file for ansible
			# override global certain global settings

			[defaults]
			# default to inventory file of ./hosts
			inventory = ./hosts
			roles_path = ./
			filter_plugins = plugins/filter
			interpreter_python  = /Users/cpuskarz/.virtualenvs/p3_aci/bin/python
			host_key_checking = False

In the snippet above you see the __interpeter_python__ environment indicated - you'll need to edit this to point to your venv.

