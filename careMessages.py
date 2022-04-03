from index import *
with open('careMessages.json') as f:
	careMessages = json.load(f)


	
# create timezones array?

func createCareMessage():
	response = ''
	for timezone in timezones:
		response += timezoneCareMessage(r.choice(careMessages[careMessages['index'][currentHour(timezone)]]))
	
# Find hour function 'currentHour'
	
