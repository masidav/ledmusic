import serial as ser
from time import sleep
class Arduino():
	def __init__(self):
		try:
			self.ard=ser.Serial('COM3')
			sleep(5)
			print("Connection Open")
			self.use=True
		except:
			print('No port')
			self.use=False
	def send_py(self, output):
		if self.use:
			gate = True
			self.ard.write(bytes(output, 'UTF-8'))
			sleep(5)
			print("Sent")
			print('Theme: ' + output)