import paramiko
command = 'ls '
HOST = 'enter_APIC_ip_address'

# Here's a script example on how to ssh into the APIC using keys
# Enter the HOTST IP address above and the commands you'd like to try
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    #client.connect(hostname = HOST, key_filename='/path_to_private_key')

    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())
    print(stderr.read())

finally:
    client.close()

