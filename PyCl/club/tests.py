from django.test import TestCase 
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event;
from .forms import MeetingForm, ResourceForm;
from django.urls import reverse_lazy, reverse
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

class NewMeetingForm(TestCase):
    def test_meetingform(self):

        data={'meetingtitle':'hey', 'meetingtime':'04-25-2022', 'meetinglocation': 'here', 'meetingdate': '04-25-2022', 'meetingagenda': 'learning',}
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='Leteletelete12')
        self.type=Resource.objects.create(resourcename='Business prep', resourcetype="type", minutestext='oo', dateentered="1983-05-14", userid=self.test_user, url='whatever.com')
        self.resource=Resource.objects.create(resourcename='test', resourcetype="type", minutestext='oo', dateentered="1983-05-14", userid=self.test_user, url='whatever.com')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')