## These scripts are from Cisco DevNet

### To Use

Edit the 'inventory' file credentials for your setup. These scripts build upon each other; so you need to run 001 and 002 at a minimum. To run the remaining scripts, you'll need to edit a few files in the in the "vars" directory. Edit these to point to your tenant that you created in 001.


- 001 tenant: 
	
		ansible-playbook 001-aci-tenant-pb.yml -i inventory	
- 002 network:

		ansible-playbook 002-aci-tenant-network-pb.yml -i inventory --extra-vars "vrf=prod_vrf"

- 003 policies:
		
		ansible-playbook 003-aci-tenant-policies-pb.yml -i inventory -vvv
		
- 004 app:

		ansible-playbook 004-aci-tenant-app-pb.yml -i inventory --extra-vars "@./vars/intranet_vars.yml"
		
	
- 005 deploy app:

		ansible-playbook 005-aci-deploy-app.yml -i inventory --list-tasks
	
		ansible-playbook 005-aci-deploy-app.yml -i inventory --extra-vars "@./vars/intranet_vars_full_config.yml" --tags bd
		
- 006 REST:

		ansible-playbook 006-aci-rest-pb.yml -i inventory
		
- 007 Cleanup:

		ansible-playbook 007-lab-cleanup.yml -i inventory

