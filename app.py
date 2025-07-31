import psutil
import time
import libcmdctrl

def network_name_selector():
	connections = psutil.net_io_counters(pernic = True)
	network_names = []
	print('Those are the devices detected, Type the name of the device if ')
	print('the desired device is found or press r to reload: \n\n')
	
	for element in connections:
		network_names.append(f'{element}')
	
	for element in network_names:
		print(f"[{network_names.index(element)}] - {element}")
	
	global response
	response = input('ANS: ')
	
	if response == 'r' or response == 'R':
		print("Restarting...")
		time.sleep(1.5)
		libcmdctrl.clear()
		network_name_selector()

	try:
		response = int(response)
	except ValueError:
		print('Input Error')
		time.sleep(1.5)
		libcmdctrl.clear()
		network_name_selector()
	
	try:
		if network_names[response] in connections:
			return network_names[response]
	except:
		print('The Number you entered is bigger than available')
		time.sleep(1.5)
		libcmdctrl.clear()
		network_name_selector()


def run():
	network_name = network_name_selector()
	
	libcmdctrl.clear()

	while True:
		networks     = psutil.net_io_counters(pernic = True)
		for element in networks.items():
			if element[0] == network_name:
				print(f"Network Name:     {element[0]}")
				print("=================================================")
				print(f"       Data sent: {element[1][0] / 1024.0 / 1024.0} MB")
				print(f"   Data Recieved: {element[1][1] / 1024.0 / 1024.0} MB")
				print(f"    Packets sent: {element[1][2]} Packets")
				print(f"Packets Recieved: {element[1][3]} Packets")
		time.sleep(0.5)
		libcmdctrl.clear()
		libcmdctrl.set_cursor_position(0, 0)


run()