# ACI: Curling

### Bootstrapping
I suggest using a virtualenv while running these. We'll need to install libraries from time to time.

### Getting Started
This the shortened reference guide version on how to use CURL to access ACI API's. 

Reference: 

* https://unofficialaciguide.com/category/all/
* https://unofficialaciguide.com/2019/01/17/best-practices-for-curling/
* https://unofficialaciguide.com/2018/12/20/getting-started-with-curl/

Here's a few examples, edit commands to provide username and password. Example: name=admin, pwd=hello. Also delete the COOKIE as needed.

- Login and returns a cookie, but hard to use for subsequent curl's
	* `curl -k -X POST -d "<aaaUser name=admin pwd=hello/>" https://10.91.86.180/api/mo/aaaLogin.xml`

- Login and save the COOKIE
	* `curl -s -k -d "<aaaUser name=admin pwd=hello/>" -c COOKIE -X POST http://10.91.86.180/api/mo/aaaLogin.xml`

- Then, you simply use “-b COOKIE” in subsequent requests, such as retrieving a list of tenants
	* `curl -s -k -X GET https://10.91.86.180/api/node/class/fvTenant.xml -b COOKIE` 

- You can pass XML output through the xmllint utility to format (indent) it:
	* `curl -s -k -X GET https://10.91.86.180/api/node/class/fvTenant.xml -b COOKIE | xmllint --format -`

- Another way to do this is to save the output to a file, and then read the file using xmllint
	* `curl -s -k -X GET https://10.91.86.180/api/node/class/fvTenant.xml -b COOKIE -o tenants.xml`
`xmllint --format tenants.xml`

- Using JSON, you can use a tool called json_pp (“pretty print”) to get nice formatting:
	* `curl -s -k -X GET https://10.91.86.180/api/node/class/fvTenant.json -b COOKIE | json_pp`


This link goes into deeper details on to use [CURL to configure ACI.](https://unofficialaciguide.com/2019/01/17/best-practices-for-curling/)


### Other Stuff
There are some Python scripts in progress in this repo
	
* SSH into the APIC using keys (edit file for commands and IP address)
* Get attached EP's (edit file to provide controller, user and password)

	


