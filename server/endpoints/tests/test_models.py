from django.test import TestCase
from endpoints.models import User, Event, Ticket, Participant
from datetime import datetime

class UserModelTest(TestCase):
    '''
        Testing User model
    '''
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            fname='Saifur',
            lname='Rahman',
            mail='test@gmail.com',
            contact_number='9112541976'
        )
    
    def test_fname_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.fname}'
        self.assertEqual(expected_object_name,'Saifur')

    def test_lname_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.lname}'
        self.assertEqual(expected_object_name,'Rahman')
    
    def test_mail_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.mail}'
        self.assertEqual(expected_object_name,'test@gmail.com')

    def test_contact_number_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.contact_number}'
        self.assertEqual(expected_object_name,'9112541976')


class EventModelTest(TestCase):
    '''
        Testing Event model
    '''
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            fname='Saifur',
            lname='Rahman',
            mail='test@gmail.com',
            contact_number='9112541976'
        )
        Event.objects.create(
            prize='iphone',
            winner=User.objects.get(id=1),
            date=datetime(2021,4,8,3,29,5)
        )
    
    def test_prize_content(self):
        event = Event.objects.get(id=1)
        expected_object_name = f'{event.prize}'
        self.assertEqual(expected_object_name,'iphone')

    def test_winner_content(self):
        event = Event.objects.get(id=1)
        winner = User.objects.get(id=1)
        expected_object_name = f'{event.winner}'
        self.assertEqual(expected_object_name,winner.fname + " " + winner.lname)

    def test_date_content(self):
        event = Event.objects.get(id=1)
        expected_object_name = f'{event.date}'
        self.assertEqual(expected_object_name,'2021-04-08 03:29:05+00:00')


class TicketModelTest(TestCase):
    '''
        Testing Ticket model
    '''
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            fname='Saifur',
            lname='Rahman',
            mail='test@gmail.com',
            contact_number='9112541976'
        )
        Ticket.objects.create(
            user=User.objects.get(id=1),
            count=5
        )
    
    def test_user_content(self):
        ticket = Ticket.objects.get(id=1)
        user = User.objects.get(id=1)
        expected_object_name = f'{ticket.user}'
        self.assertEqual(expected_object_name, user.fname + ' ' + user.lname)
    
    def test_count_content(self):
        ticket = Ticket.objects.get(id=1)
        expected_object_name = ticket.count
        self.assertEqual(expected_object_name, 5)


class ParticipantModelTest(TestCase):
    '''
        Testing Participant model
    '''
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            fname='Saifur',
            lname='Rahman',
            mail='test@gmail.com',
            contact_number='9112541976'
        )
        Ticket.objects.create(
            user=User.objects.get(id=1),
            count=5
        )
        Event.objects.create(
            prize='iphone',
            winner=User.objects.get(id=1),
            date=datetime(2021,4,8,3,29,5)
        )
        Participant.objects.create(
            event=Event.objects.get(id=1),
            ticket=Ticket.objects.get(id=1)
        )

    def test_ticket_content(self):
        participant = Participant.objects.get(id=1)
        ticket = Ticket.objects.get(id=1)
        expected_object_name = participant.ticket
        self.assertEqual(expected_object_name, ticket)

    def test_event_content(self):
        participant = Participant.objects.get(id=1)
        event = Event.objects.get(id=1)
        expected_object_name = participant.event
        self.assertEqual(expected_object_name, event)