from django.db import models

class PortfolioEntry(models.Model):
    class Category(models.TextChoices):
        CONCEPT_ART = 'CA', 'Concept Art'
        ANIMATION = 'AN', 'Animation'
        ILLUSTRATION = 'IL', 'Illustration'
        OTHER = 'OT', 'Other'

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/portfolio/')
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.OTHER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
