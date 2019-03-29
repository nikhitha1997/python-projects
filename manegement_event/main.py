from models import * 

def add_events():
	event_name=input('enter the name of the event want to add:')
	EventList.create(event_name=event_name)

def see_events():
	events=EventList.select()
	for event in events:
		print(event.id,event.event_name,sep='-')

def add_participants():
	participant_name=input('enter the name of the participant:')
	events=EventList.select()
	for event in events:
		print(event.id,event.event_name,sep='-')
		event_id=int(input('select the event in which the participant wants to participate:\n'))
		ParticipantList.create(participant_name=participant_name,event_name=event_id)

def see_participants():
	for participant in ParticipantList.select():
		print(participant.id,participant.participant_name,EventsList.get(participant.events_name_id).events_name.name,sep='-')



while True:
	choice= input('enter the action that u want to do:\n 1.Add event \n 2.see event\n\n 3.Add participant\n 4.see participant\n 5.exit\n')
	if choice=='1':
		add_events()
	elif choice=='2':
		see_events()
	elif choice=='3':
		add_participants()
	elif choice=='4':
		see_participants()
	else:
		break
