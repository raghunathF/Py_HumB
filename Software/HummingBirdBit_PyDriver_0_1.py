############################################################################################
#	Author				Raghunathreddy Jangam 
#   Date                06/26/2018
#   Description         Python driver for HummingBirdBit
############################################################################################

##Stage --1
##Checking if senfing URL works

# import urllib.request
# while (1):
# 	url = "http://127.0.0.1:30061/hummingbird/in/orientation/Screen%20Up/A"
# 	print(url)
# 	f =  urllib.request.urlopen(url)
# 	output = f.read()
# 	output = output.decode('utf-8') 
# 	print(output)
	# print(int(output))
	# output = int.from_bytes(output,byteorder="little",signed = "true")
	# print(output)

# # import pyttsx3
# # engine = pyttsx3.init()
# # engine.say('Good morning.')
# # engine.runAndWait()

from HummingBird_Bit import Hummingbird,Microbit
import time

# def collect_device_names (no_dev_conn):
# 	for i in range(1,no_dev_conn):
# 		names_devices[i] = device_name(i)

# def check_BLE_devices:
# 	check_adapter()
# 	no_dev_conn = check_devices()
# 	collect_device_names(no_dev_conn)


def main():
	# check_BLE_devices()
	bird1 = Hummingbird('A')
	bird2 = Microbit('B')
	while(1):
		# bird1.setPositionServo(1,100)
		# bird1.setLED(1,100)
		# bird1.setTriLED(1,100,100,100)
		# bird1.plot(2,0,0)
		# bird1.printAndWait("RAGHU")
		
		# time.sleep(0.1) 
		# bird1.setPositionServo(1,0)
		# bird1.setLED(1,0)
		# bird1.setTriLED(1,0,0,0)
		# bird1.plot(0,0,1)
		# time.sleep(0.1) 
		# bird1.setDisplay( 		"10000"\
		# 						"01000"\
		# 			 		    "00100"\
		# 			 			"00010"\
		# 			 			"00001")
		# bird2.setDisplay( 		"10000"\
		# 						"01000"\
		# 			 		    "00100"\
		# 			 			"00010"\
		# 			 			"00001")
		# time.sleep(0.1) 
		# bird1.setDisplay( 		"00100"\
		# 						"00100"\
		# 			 		    "00100"\
		# 			 			"00100"\
		# 			 			"00100")
		# bird2.setDisplay( 		"00100"\
		# 						"00100"\
		# 			 		    "00100"\
		# 			 			"00100"\
		# 			 			"00100")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"00001"\
		# 						"00010"\
		# 			 		    "00100"\
		# 			 			"01000"\
		# 			 			"10000")
		# bird2.setDisplay( 		"00001"\
		# 						"00010"\
		# 			 		    "00100"\
		# 			 			"01000"\
		# 			 			"10000")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"00000"\
		# 						"00000"\
		# 			 		    "11111"\
		# 			 			"00000"\
		# 			 			"00000")
		# bird2.setDisplay( 		"00000"\
		# 						"00000"\
		# 			 		    "11111"\
		# 			 			"00000"\
		# 			 			"00000")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"10000"\
		# 						"01000"\
		# 			 		    "00100"\
		# 			 			"00010"\
		# 			 			"00001")
		# bird2.setDisplay( 		"10000"\
		# 						"01000"\
		# 			 		    "00100"\
		# 			 			"00010"\
		# 			 			"00001")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"00100"\
		# 						"00100"\
		# 			 		    "00100"\
		# 			 			"00100"\
		# 			 			"00100")
		# bird2.setDisplay( 		"00100"\
		# 						"00100"\
		# 			 		    "00100"\
		# 			 			"00100"\
		# 			 			"00100")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"00001"\
		# 						"00010"\
		# 			 		    "00100"\
		# 			 			"01000"\
		# 			 			"10000")
		# bird2.setDisplay( 		"00001"\
		# 						"00010"\
		# 			 		    "00100"\
		# 			 			"01000"\
		# 			 			"10000")
		# time.sleep(0.1)
		# bird1.setDisplay( 		"00000"\
		# 						"00000"\
		# 			 		    "11111"\
		# 			 			"00000"\
		# 			 			"00000")
		# bird2.setDisplay( 		"00000"\
		# 						"00000"\
		# 			 		    "11111"\
		# 			 			"00000"\
		# 			 			"00000")
		# time.sleep(0.1)
		value = bird1.getLight(1)
		value1,value2,value3 = bird1.getMagnetometer()
		value = bird1.getOrientation()

		#value = bird1.getCompass()
		time.sleep(0.1)
		#print(value)
		#print(value1,value2,value3)

if __name__ == '__main__':
	main()