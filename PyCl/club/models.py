from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingtime=models.DateField()
    meetingdate=models.DateField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.CharField(max_length=255)

    

    def __str__(self):
        return self.meetingminutesname
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    minutestext=models.CharField(max_length=255)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()
    url=models.URLField()


    

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eventlocation=models.TextField()
    eventdescription=models.CharField(max_length=255)
        
    def __str__(self):
        return self.eventname
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'




