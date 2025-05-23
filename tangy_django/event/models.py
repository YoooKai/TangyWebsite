from django.db import models

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/events/')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  
    location = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)  
    location_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['start_date']  

    def __str__(self):
        return self.title

    def is_multi_day(self):
        return self.end_date and self.start_date != self.end_date
