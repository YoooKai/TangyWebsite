from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from django.conf import settings
from django.core.mail import send_mail

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    STATUS_CHOICES = [
        ('processing', 'En proceso'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),  
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='processing',
    )

    tracking_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.first_name
    
    
    def save(self, *args, **kwargs):
        is_new_instance = self._state.adding
        previous_status = None

        if not is_new_instance:
            try:
                previous = Order.objects.get(pk=self.pk)
                previous_status = previous.status
            except Order.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        if previous_status != 'shipped' and self.status == 'shipped':
            self.send_tracking_email()

    def send_tracking_email(self):
        if not self.email or not self.tracking_number:
            return  

        subject = 'Tu pedido ha sido enviado 🚚'
        message = (
            f"Hola {self.first_name},\n\n"
            f"Tu pedido ha sido enviado y está en camino. "
            f"Aquí tienes tu número de seguimiento:\n\n"
            f"📦 Tracking: {self.tracking_number}\n\n"
            f"Gracias por comprar con nosotros.\n\n"
            f"Tangerine Mess"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    selected_option = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return '%s' % self.id