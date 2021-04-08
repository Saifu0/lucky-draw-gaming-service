from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User, Event, Ticket, Participant
from datetime import datetime

class TestSetUp(APITestCase):
    def setUp(self):
        '''
            Populating temporary database
        '''
        self.user = User.objects.create(
            fname='Gufran',
            lname='Khan',
            mail='test@gmail.com',
            contact_number='9112541976'
        )
        self.event = Event.objects.create(
            prize='iphone',
            winner=User.objects.get(id=1),
            date=datetime(2021,4,7,3,29,5)
        )
        self.event_2 = Event.objects.create(
            prize='trip to goa',
            winner=None,
            date=datetime(2021,4,12,3,29,5)
        )
        self.ticket = Ticket.objects.create(
            user=User.objects.get(id=1),
            count=5
        )
        self.ticket_2 = Ticket.objects.create(
            user=User.objects.get(id=1),
            count=0
        )
        self.participate = Participant.objects.create(
            event=Event.objects.get(id=1),
            ticket=Ticket.objects.get(id=1)
        )

        ''' 
            Defining URLs required for calling HTTP methods
        '''
        self.get_upcoming_event_url = reverse('get-upcoming-events')
        self.participation_url = reverse('participate-in-event')
        self.last_week_winner_url = reverse('get-last-week-winners')

        '''
            JSON object to pass into the body of POST method
        '''
        self.valid_participation_data_1 = {
            'event_id' : 1,
            'ticket_id' : 1
        }
        self.valid_participation_data_2 = {
            'event_id' : 2,
            'ticket_id' : 1
        }
        self.invalid_participation_data_1 = {
            'event_id' : 1,
            'ticket_id' : 4
        }
        self.invalid_participation_data_2 = {
            'event_id' : 3,
            'ticket_id' : 1
        }
        self.participation_with_zero_number_of_tickets = {
            'event_id' : 2,
            'ticket_id' : 2
        }
        return super().setUp()