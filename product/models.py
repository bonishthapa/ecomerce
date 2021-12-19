from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear'),
)

LABEL_CHOICES = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'Danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=50)
    discount_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("product",kwargs={
            'slug':self.slug
        })  

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)    

@receiver(pre_save, sender=Item)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)