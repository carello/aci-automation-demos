#configure provider with your cisco aci credentials.
provider "aci" {
  # cisco-aci user name
  username = "${var.username}"
  # cisco-aci password
  password = "${var.password}"
  # cisco-aci url
  url = "${var.url}"
  insecure = true
  #proxy_url    = "https://proxy_server:proxy_port"
}

resource "aci_tenant" "test-tenant" {
  name        = "test-tenant"
  description = "This tenant is created by terraform"
}

resource "aci_application_profile" "test-app" {
  tenant_dn   = "${aci_tenant.test-tenant.id}"
  name        = "test-app"
  description = "This app profile is created by terraform"
}
