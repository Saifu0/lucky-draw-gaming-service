from datetime import datetime, timedelta, timezone
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
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

# class GetTickets():