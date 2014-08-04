import serial
import time
from xbee import ZigBee
import json, requests

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
headers = {'Content-type': 'application/json'}

def print_data(data):
	frame = {
		'source_addr_long' : data['source_addr_long'].encode('hex'),
		'samples' : data['samples']
	}
	print requests.post('http://127.0.0.1:5000/api/update', data=json.dumps(frame), headers=headers)
	
xbee = ZigBee(serial_port, callback=print_data)
while True:
	try:
		time.sleep(0.02)
	except KeyboardInterrupt:
		break
		
xbee.halt()
serial_port.close()