from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.fname + " " + self.lname


class Event(models.Model):
    prize = models.CharField(max_length=100)
    winner = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.prize


class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.fname
        
    
class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return event.prize