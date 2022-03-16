from netmiko import ConnectHandler
import os

def netmiko_save_output():
	"""Connect to device and return connection object"""
	password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
	arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
	
	net_connect = ConnectHandler(**arista1)
	
	commands = ['ls']
	
	with open("cmdoutput.txt", "w") as nf:
		for _line in commands:
			output = net_connect.send_command(_line)
			nf.write(output)
	
    net_connect.disconnect()

def netmiko_ftp():
	ip_addr = '10.10.10.10'
	my_pass = getpass()
	
	net_device = {
        'device_type': 'cisco_asa',
        'ip': ip_addr,
        'username': 'admin',
        'password': my_pass,
        'secret': my_pass,
        'port': 22,
    }
	
	ssh_conn = ConnectHandler(**net_device)
	
	# ADJUST TO TRANSFER IMAGE FILE
    dest_file_system = 'disk0:'
    source_file = 'test1.txt'
    dest_file = 'test1.txt'
    alt_dest_file = 'asa825-59-k8.bin'
    scp_changed = False
	
	with FileTransfer(ssh_conn, source_file=source_file, dest_file=dest_file,
                      file_system=dest_file_system) as scp_transfer:
		if not scp_transfer.check_file_exists():
			if not scp_transfer.verify_space_available():
				raise ValueError("Insufficient space available on remote device")
				
			print "Enabling SCP"
			output = asa_scp_handler(ssh_conn, mode='enable')
			print output
			
			print "\nTransferring file\n"
			scp_transfer.transfer_file()
			
			print "Disabling SCP"
			output = asa_scp_handler(ssh_conn, mode='disable')
			print output
			
		print "\nVerifying file"
		if scp_transfer.verify_file():
			print "Source and destination MD5 matches"
		else:
			raise ValueError("MD5 failure between source and destination files")
	
	
	