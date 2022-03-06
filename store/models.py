from django.db import models
from django.conf import settings
from django.shortcuts import reverse
CATEGORY_CHOICES = (
    ('HS', 'Headset'),
    ('MC', 'Mic'),
    ('SB', 'Sound Box'),
    ('KB', 'Keyboard'),
    ('MS', 'Mouse'),
    ('MB', 'Motherboard'),
    ('HD', 'Hard Drive')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

def itemImage(instance, filename):
    return f"{instance.id}-{filename}"

class Item(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=1500, null=False)
    price = models.FloatField(null=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=False)
    label = models.CharField(choices= LABEL_CHOICES, max_length=1, null=False)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to=itemImage,
        blank=True,
        null=True
    )
    more_information = models.TextField(max_length=1500, null=False)
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(OrderItem)
    start_date =  models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
