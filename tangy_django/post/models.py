from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    class Category(models.TextChoices):
        ARTIST_ALLEY = 'AL', 'Artist Alley'
        DAILY_LIFE = 'DL', 'Daily Life'
        OTHER = 'OT', 'Other'
        ANNOUNCEMENT = 'AN', 'Announcement'

    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.OTHER
    )
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        ordering = ['-created_at']


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/blog_posts/')
    caption = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"Image for: {self.post.title}"
