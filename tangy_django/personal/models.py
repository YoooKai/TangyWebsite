from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()  
    image = models.ImageField(upload_to='media/about/', blank=True, null=True)

    def __str__(self):
        return self.title or "About Me"

class Commissions(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slots_left = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/comissions/', blank=True, null=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField() 

    def __str__(self):
        return self.question


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
