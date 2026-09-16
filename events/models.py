from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    related_name='events'
    )

    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', 
    blank=True, null=True
    )

    organizer = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,
         related_name='organized_events'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class EventSession(models.Model):
    event = models.ForeignKey(Event, 
    on_delete=models.CASCADE, 
    related_name='sessions')

    date = models.DateField()                                          
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.PositiveIntegerField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError(
                "Start time must be before end time."
                )
        overlapping_sessions = EventSession.objects.filter(
            event=self.event,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk)

        if overlapping_sessions.exists():
            raise ValidationError(
                "This session overlaps with an existing session."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.event.title} - {self.date}"


class Booking(models.Model):
    user = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE, 
        related_name='bookings'
    )
    session = models.ForeignKey(
        EventSession, 
        on_delete=models.CASCADE, 
        related_name='bookings'
    )
    booking_reference = models.CharField(
    max_length=20, 
    unique=True)
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
    max_length=20, 
    default='confirmed')
    def __str__(self):
        return self.booking_reference

