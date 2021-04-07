from django.urls import path
from .views import (
    TicketView, 
    UpcomingEventListView,
    EventParticipationView,
    LastWeekWinnersView,
    EventWinner
)

urlpatterns = [
    path('tickets/<int:user_id>',TicketView.as_view(),name="get-tickets"),
    path('upcoming-events', UpcomingEventListView.as_view(),name="get-upcoming-events"),
    path('participate',EventParticipationView.as_view(),name="participate-in-event"),
    path('past-winners',LastWeekWinnersView.as_view(),name="get-last-week-winners"),
    path('event-winner/<int:event_id>',EventWinner.as_view(),name="get-or-compute-winner")
]
