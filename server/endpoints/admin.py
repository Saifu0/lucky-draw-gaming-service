from django.contrib import admin
from .models import User, Event, Ticket, Participant

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Participant)
