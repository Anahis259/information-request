import re
zipCode_string=input("Enter a valid zip code: ")
match_zipcode=re.search('^\d{5}-\d{4}$',zipCode_string)

if match_zipcode:
	print('Valid zip code')
else:
	print('Not valid zip code')
	