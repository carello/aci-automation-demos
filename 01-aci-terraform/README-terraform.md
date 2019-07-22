## Terraform and ACI

### To Use

- Edit the `terraform.tfvars` file to provide your username, password, and URL.
- Run `terraform init`
- Run `terraform apply`

When Terraform runs, it creates a file called "terraform.tfstate" to keep track of state. However, for this simple example, delete this file if you want to re-run the application. Also, don't forget to delete the Tenant in ACI before running.

