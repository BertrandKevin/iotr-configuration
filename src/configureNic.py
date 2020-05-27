#!/usr/bin/python

import os
import platform

import src.check_user_input as checkUserInput

def set_nic_settings(aftr, countryCode):
	if "Core" not in platform.platform():
		print("Ce n'est pas Ubuntu Core")

		# Country Code configuration
		try:
			command = "sudo netmgr -i country_code set:" + countryCode
			os.system(command)
		except:
			print("Le country code n'a pas pu etre configure!")

		# AFTR configuration
		try:
			command = "sudo netmgr -i iotr aftr_address set " + aftr
			os.system(command)
		except:
			print("L'AFTR n'a pas pu etre configuree!")

		# Network ID configuration
		print("Le network ID ne peut pas etre configure par ce programme, il doit se faire pas l'interface web!")

	else:
		print("C'est Ubuntu Core")

		# Country Code configuration
		try:
			command = "itron-edge.netmgr -i country_code set:" + countryCode
			os.system(command)
		except:
			print("Le country code n'a pas pu etre configure!")

		# AFTR configuration
		try:
			command = "itron-edge.netmgr -i aftr_address set " + aftr
			os.system(command)
		except:
			print("L'AFTR n'a pas pu etre configuree!")

		# Network ID configuration
		print("Le network ID ne peut pas etre configure par ce programme, il doit se faire pas l'interface web!")

def get_nic_settings():
	countryCode = 0
	aftr = ""
	networkId = 0

	while True:
		try:
			countryCode = int(input("Encodez le country code"))
			question = "Validez-vous le country code " + str(countryCode) + " ?\n[y]: Oui\n[n]: Non\nReponse: "

			if checkUserInput.question_and_verification(question) == "y":
				break
			else:
				print("Le country code n'a pas ete valide! Veuillez en encoder un nouveau!")

		except:
			print("Le country code n'est pas valide!")

	while True:
		answer = input("Encodez l'adresse AFTR: ")
		question = "Validez-vous l'AFTR " + aftr + " ?\n[y]: Oui\n[n]: Non\nReponse: "

		if checkUserInput.question_and_verification(question) == "y":
			break
		else:
			print("L'AFTR n'a pas ete validee! Veuillez en encoder une nouvelle!")

	set_nic_settings(aftr, countryCode)