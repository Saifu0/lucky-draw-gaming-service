from datetime import datetime, timedelta, timezone
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from .models import User, Event, Ticket, Participant
from .serializers import (
    UserSerializer,
    EventSerializer,
    TicketSerializer,
    ParticipantSerializer
)
import random


class TicketView(APIView):
    '''
        This API view will allow the users to get raffle tickets.
        By default, it will assign 2 tickets to a user but user can ask
        for more than 2 not greater than 5 tickets at a time.

        get method:
            user_id is ID of requested user
            request.query_params.get("count") is number of ticket count user wants at a time ( max : 5)
        
        generate_tickets:
            paramters : number_of_tickets, user
            This method will add valid requested tickets into the user account
    '''
    def get(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response({
                "error" : "Invalid User!"
            }, status = HTTP_400_BAD_REQUEST)

        number_of_tickets = self.request.query_params.get("count")
        if number_of_tickets is None:
            number_of_tickets = 2
        number_of_tickets = int(number_of_tickets)
        
        if number_of_tickets > 5 or number_of_tickets < 1:
            return Response({
                "error" : "Number of ticket counts should be between 1 to 5"
            })
        
        resp = self.generate_tickets(number_of_tickets,user)

        return Response({
            "success" : f"{number_of_tickets} ticket(s) have been added for user {user.fname} {user.lname}"},
            status = HTTP_200_OK
            )

    def generate_tickets(self,number_of_tickets,user):
        try:
            ticket = Ticket.objects.get(user=user)
            ticket.count += number_of_tickets
            ticket.save()
        except:
            ticket = Ticket(user=user, count=number_of_tickets)
            ticket.save()
        return ticket




class UpcomingEventListView(ListAPIView):
    '''
        GET method for getting list of Upcoming events
    '''
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(date__gte=datetime.now(timezone.utc))
        return queryset
    



class EventParticipationView(APIView):
    '''
        This API view will allow the users to participate in the events if they have enough tickets.
        Already participated user in an event cannot participate again in the same events.

        post method:
            body will contain 2 data: 1. event ID 2. ticket ID
    '''
    def post(self,request):
        try: 
            ticket_id = self.request.data['ticket_id']
        except:
            return Response({
                "error" : "ticket ID is required!"
            }, status = HTTP_400_BAD_REQUEST)
        try:
            event_id = self.request.data['event_id']
        except:    
            return Response({
                "error" : "event ID is required!"
            }, status = HTTP_400_BAD_REQUEST)


        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except:
            return Response({
                "error" : "Invalid Ticket ID."
            }, status = HTTP_400_BAD_REQUEST)
        try:
            event = Event.objects.get(id=event_id)
        except:
            return Response({
                "error" : "Invalid Event ID."
            }, status = HTTP_400_BAD_REQUEST)

        
        if ticket.count == 0:
            return Response({
                "error" : "User have no ticket."
            }, status = HTTP_400_BAD_REQUEST)


        if Participant.objects.filter(ticket=ticket,event=event).count() > 0:
            return Response({
                "error" : "Already participated!" 
            }, status = HTTP_400_BAD_REQUEST)
        
        participate = Participant(ticket=ticket,event=event)
        participate.save()

        ticket.count -= 1
        ticket.save()
        
        return Response({
            "success" : "Successfully participated, Wish you Best of Luck!"
        }, status = HTTP_201_CREATED)




class LastWeekWinnersView(APIView):
    '''
        This API view will allow users to fetch winner of all the events in the last one week.
    '''

    def get(self, request):
        last_week_date = self.get_last_week_date()
        print(last_week_date)
        queryset = EventSerializer(Event.objects.filter(date__gte=last_week_date).exclude(winner=None),many=True).data
        return Response(queryset, status = HTTP_200_OK)

    def get_last_week_date(self):
        date = datetime.now(timezone.utc) - timedelta(days=7)
        return date




class EventWinner(APIView):
    '''
        This API view will allow users to compute the winner of the event.
        Once winner is declared, (S)he will not change.

        get method:
            paramter: event ID
            This method will compute(if not already computed) winner of the event
            If already computed, then just return Name of winner.  
    '''
    def get(self,request,event_id):
        try:
            event = Event.objects.get(id=event_id)
        except:
            return Response({
                "error" : "Invalid Event ID!"
            }, status = HTTP_400_BAD_REQUEST)
        
        if event.winner != None:
            return Response({
                "response" : f"Winner already announced! Winner was {event.winner.fname} {event.winner.lname}." 
            }, status = HTTP_200_OK)
        
        participants = Participant.objects.filter(event=event)

        if participants.count() == 0:
            return Response({
                "error" : "No one participated yet!"
            }, status = HTTP_200_OK)
        
        winner = random.choice(participants)
        event.winner = winner.ticket.user
        event.save()

        return Response({
            "success" : f"Event ID: {event_id}, Winner: {event.winner.fname} {event.winner.lname}"
        }, status = HTTP_200_OK)