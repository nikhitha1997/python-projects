import peewee
db=peewee.SqliteDatabase('events.db')#database

class EventList(peewee.Model):  #link creat bw two table called foreign key
	event_name=peewee.TextField()

	class Meta:
		database=db  #meta is used to connect the information with db

class ParticipantList(peewee.Model):
	participant_name=peewee.TextField()
	event_name = peewee.ForeignKeyField(EventList)

	class Meta:
		database=db	
db.connect()
db.create_tables([EventList,ParticipantList])		
