#!/user/bin/env python

import signal
import buttonshim
import time
import subprocess

print("""
	Pi-Hole Button Control Running....

	Press Ctrl+C to Exit.
	""")

#Cycle and clear LEDs on startup (visual indication the script is running)
buttonshim.set_pixel(255,0,0)
time.sleep(0.3)
buttonshim.set_pixel(0,255,0)
time.sleep(0.3)
buttonshim.set_pixel(0,0,255)
time.sleep(0.3)
buttonshim.set_pixel(0,0,0)
pressId = 0

while True:
	def DisablePiholeTimer(numSecs):
		global pressId
		loopId = pressId
		for i in range(0,numSecs):
			if ( loopId != pressId):
				print "Ending loop with ID: " + str(loopId)
				return
			print "Pi-Hole disabled for " + str(numSecs-i)
			buttonshim.set_pixel(255,255,0)
			time.sleep(0.5)
			buttonshim.set_pixel(255,150,0)
			time.sleep(0.5)
		buttonshim.set_pixel(0,0,0)
		print "Pi-Hole reenabled"

	def SuspendPihole():
		global pressId
		loopId = pressId
		print "Pi-Hole suspended"
		while (loopId == pressId):
			buttonshim.set_pixel(255,0,0)
			time.sleep(0.5)
			buttonshim.set_pixel(0,0,0)
			time.sleep(0.5)

	def EnablePihole():
		global pressId
		loopId = pressId
		print "Pi-Hole enabled"
		for i in range(0,2):
			buttonshim.set_pixel(0,255,0)
			time.sleep(0.3)
			buttonshim.set_pixel(0,0,0)
			time.sleep(0.3)


	@buttonshim.on_press(buttonshim.BUTTON_A)
	def button_a(button, pressed):
		print "Disabling Pi-Hole for 300s"
		global pressId
		pressId += 1
		subprocess.call(['pihole','disable','300s'])
		DisablePiholeTimer(int(300))

	@buttonshim.on_press(buttonshim.BUTTON_B)
	def button_b(button, pressed):
		print "Disabling Pi-Hole for 1800s"
		global pressId
		pressId += 1
		subprocess.call(['pihole','disable','1800s'])
		DisablePiholeTimer(int(1800))

	@buttonshim.on_press(buttonshim.BUTTON_C)
	def button_c(button, pressed):
	        print "This button, it does nothing"

	@buttonshim.on_press(buttonshim.BUTTON_D)
	def button_d(button, pressed):
		print "Suspending Pi-Hole"
		global pressId
		pressId += 1
		subprocess.call(['pihole','disable'])
		SuspendPihole()

	@buttonshim.on_press(buttonshim.BUTTON_E)
	def button_e(button, pressed):
		print "Enabling Pi-Hole"
		global pressId
		pressId += 1
		subprocess.call(['pihole','enable'])
		EnablePihole()



	signal.pause()
