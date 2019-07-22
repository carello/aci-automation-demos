# ACI: Postman and Runner Examples
---

#### This demo has two parts

Part A Collection consists of:

* A collection with an extensive inventory of GET and POST API commands, approx 53.
* The collection includes environmental parameters that you'll need to customize for your setup; e.g., IP-Address, Password, Tenant etc..

Part B is a Runner Collection:

* Inside the Collection is a folder called "running_example". This is a simple REST call that creates a Bride Domain and Subnet.
* There's a .csv file included for an example.
* The Tenant needs to be pre-configured in the APIC. See the "To Use" section below.
* There's also an environment included


---

### To Use
- Import the Collection and Environments into Postman.
- After you configured your parameters in the environment, there are two POSTS that you should run first:
	* Login
	* Create Tenant and VRF

Now go ahead and play with ACI Postman! 
