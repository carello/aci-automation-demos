## Datacenter deployment "In-Depth". Created by WWT

The scripts are designed to deploy and ACI fabric and hosts. It's very extensive and would be unique to a specific fabric. However, this can be run in --check mode to see the output and all this is possible.

### To Use

Edit the credentials in: `example-inventory.yaml` for your setup

Run: `ansible-playbook -i example-inventory.yaml example-playbook.yaml --check`
