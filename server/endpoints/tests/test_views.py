from django.urls import reverse
from .test_setup import TestSetUp

class TicketViewTest(TestSetUp):
    '''
        GET request
        Testing ticket view
    '''
    def test_get_ticket_with_invalid_user_id(self):
        get_tickets_url = reverse('get-tickets', args=[2])
        res = self.client.get(get_tickets_url)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data["error"], "Invalid User!")


    def test_get_ticket_with_valid_user_id(self):
        get_tickets_url = reverse('get-tickets', args=[1])
        res = self.client.get(get_tickets_url)
        success = "2 ticket(s) have been added for user Gufran Khan"
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["success"], success)


class UpcomingEventViewTest(TestSetUp):
    '''
        GET request
        Testing upcoming events view
    '''
    def test_upcoming_event_list(self):
        res = self.client.get(self.get_upcoming_event_url)
        self.assertEqual(res.status_code,200)


class EventParticipationViewTest(TestSetUp):
    '''
        POST request
        Testing event participation view
    '''
    def test_event_participation_without_eventid_ticketid(self):
        res = self.client.post(self.participation_url)
        self.assertEqual(res.status_code,400)
        self.assertEqual(res.data['error'],'ticket ID is required!')


    def test_event_participation_with_invalid_ticketid(self):
        res = self.client.post(self.participation_url,self.invalid_participation_data_1,format='json')
        self.assertEqual(res.status_code,400)
        self.assertEqual(res.data['error'],'Invalid Ticket ID.')


    def test_event_participation_with_invalid_eventid(self):
        res = self.client.post(self.participation_url,self.invalid_participation_data_2,format='json')
        self.assertEqual(res.status_code,400)
        self.assertEqual(res.data['error'],'Invalid Event ID.')


    def test_event_participation_with_zero_number_of_tickets(self):
        res = self.client.post(self.participation_url,self.participation_with_zero_number_of_tickets,format='json')
        self.assertEqual(res.status_code,400)
        self.assertEqual(res.data['error'],"User have no ticket.")


    def test_event_participation_with_valid_data_1(self):
        res = self.client.post(self.participation_url,self.valid_participation_data_1,format='json')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data['success'],"Already participated!")


    def test_event_participation_with_valid_data_2(self):
        res = self.client.post(self.participation_url,self.valid_participation_data_2,format='json')
        self.assertEqual(res.status_code,201)
        self.assertEqual(res.data['success'],"Successfully participated, Wish you Best of Luck!")


class LastWeekWinnersViewTest(TestSetUp):
    '''
        GET method
        Testing of Last week winner view API
    '''
    def test_last_week_winner(self):
        res = self.client.get(self.last_week_winner_url)
        self.assertEqual(res.status_code,200)


class EventWinnerViewTest(TestSetUp):
    '''
        GET method
        Testing of event winner view API
    '''
    def test_event_winner_with_invalid_eventid(self):
        event_winner_url = reverse('get-or-compute-winner',args=[5])
        res = self.client.get(event_winner_url)
        self.assertEqual(res.status_code,400)
        self.assertEqual(res.data['error'],"Invalid Event ID!")


    def test_event_winner_already_announced(self):
        event_winner_url = reverse('get-or-compute-winner',args=[1])
        res = self.client.get(event_winner_url)
        self.assertEqual(res.status_code,200)


    def test_event_winner_with_valid_event_id(self):
        event_winner_url = reverse('get-or-compute-winner',args=[2])
        res = self.client.get(event_winner_url)
        self.assertEqual(res.status_code,200)