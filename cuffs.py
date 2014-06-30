#!/usr/bin/python
# Raymond Ho
# June 21, 2014
# A hidden file is created, make sure to delete it when removing cuffs.py

import os, sys

# Change this value to change key value.
key = 5
# Amount of tries the user has before data is deleted.
count = 3
fileName = ".cuffs"

def encryptString(string, key):
	charHolder = []
	for c in string:
		charHolder.append(chr(ord(c) + key))
	newString = ''.join(charHolder)
	return newString

def decryptString(string, key):
	charHolder = []
	for c in string:
		charHolder.append(chr(ord(c) - key))
	newString = ''.join(charHolder)
	return newString

def readFile():
	# Try to open file, create if does not exist
	
	f = open(fileName, "a+")
	f.seek(0)
	print decryptString(f.read(), key)
	if os.stat(fileName).st_size == 0:
		print "There is no data stored."

print "1: View passwords."
print "2: New Entry"
print "3: Delete all data"
print "4: Exit"

# Infinite loop to read input
while (True):

	mode = int(raw_input ("\nEnter your mode: "))

	if mode == 1:
		decrypt = int(raw_input("Enter your decryption key: "))
		if decrypt == key:
			readFile()
		else:
			count -= 1
			print "Wrong key, %i tries left" % count
			if count == 0:
				print "You are out of tries, deleting data."
				f = open(fileName, "w")
				f.close()

	elif mode == 2:
		whatfor = raw_input("This is for: ")
		username = raw_input("Enter your username: ")
		password = raw_input("Enter your password: ")

		#Append to end of file.
		f = open(fileName, "a+")
		original = "%s-> Username: %s, Password: %s\n" % (whatfor, username, password)
		f.write(encryptString(original, key))
		f.close()

	elif mode == 3:
		if raw_input("Enter 'yes' to confirm: ") == "yes":
			open(fileName, "w")
			print "Data successfully deleted."

	elif mode == 4:
		sys.exit(0)

	else: print "Invalid input, please try again."


