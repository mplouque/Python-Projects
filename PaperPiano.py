########################################
# Name:
# Date:
# Description: Paper piano (v1).
########################################
import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

# the note generator class
class Note(pygame.mixer.Sound):
	# note that volume ranges from 0.0 to 1.0
	def __init__(self, frequency, volume):
		self.frequency = frequency
		# initialize the note using an array of samples
		pygame.mixer.Sound.__init__(self, self.build_samples())
		self.set_volume(volume)

	# builds an array of samples for the current note
	def build_samples(self):
		# calculate the period and amplitude of the note's wave
		period = int(round(MIXER_FREQ / self.frequency))
		amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
		# initialize the note's samples (using an array of
		# signed 16-bit "shorts")
		samples = array("h", [0] * period)

		# generate the note's samples
		for t in range(period):
			if (t < period / 2):
				samples[t] = amplitude
			else:
				samples[t] = -amplitude
			
			return samples


# waits until a note is pressed
def wait_for_note_start():
	while (not GPIO.input(key)):
		sleep(0.01)

# waits until a note is released
def wait_for_note_stop():
	while (GPIO.input(key)):
		sleep(0.1)

# preset mixer initialization arguments: frequency (44.1K), size
# (16 bits signed), channels (mono), and buffer size (1KB)
# then, initialize the pygame library
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)
# setup the pin and frequency for a C note
key = 26
freq = 261.6
# setup the input pin

GPIO.setup(key, GPIO.IN, GPIO.PUD_DOWN)

# create the actual C note
note = Note(freq, 1)

# the main part of the program
print "Welcome to Paper Piano!"
print "Press Ctrl+C to exit..."
# detect when Ctrl+C is pressed so that we can reset the GPIO
# pins
try:
	while (True):
		# play a note when pressed...until released
		wait_for_note_start()
		note.play(-1)
		wait_for_note_stop()
		note.stop()
	
	except KeyboardInterrupt:
		# reset the GPIO pins
		GPIO.cleanup()
