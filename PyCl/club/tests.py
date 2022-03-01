from django.test import TestCase 
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Buisiness Prep')
    
   
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Buisiness Prep') 

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='hey')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'hey') 

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='hey')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'hey') 

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(minutestext='network')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'MeetingMinutes object (None)') 

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')