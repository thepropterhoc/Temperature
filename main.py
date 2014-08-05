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
	try:
		response = requests.post('http://localhost:80/api/update', data=json.dumps(frame), headers=headers)
		if not response.status_code == 200:
			print 'Unusual response: ' + response
	except Exception, e:
		print 'Server unavailable'
	
xbee = ZigBee(serial_port, callback=print_data)

while True:
	try:
		time.sleep(0.02)
	except KeyboardInterrupt:
		break
		
xbee.halt()
serial_port.close()
