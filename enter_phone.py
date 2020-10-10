import re 

phone_string= input("Enter a valid phone: ")

match_phone= re.search('^\+?\w+\s?\.?\d{4}\s?\.?\d{6,7}',phone_string)

if match_phone:
	print ('Valid phone')
else:

	print('Not valid phone')