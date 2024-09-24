from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

from django.db import models

#groceries categories tuple of tuples. to save data effeciently and to have a more effecient way to filter this later on
CATEGORY_CHOICES = [
    ('FR', 'Fresh Produce'),
    ('DA', 'Dairy'),
    ('MP', 'Meat and Poultry'),
    ('SF', 'Seafood'),
    ('FRZ', 'Frozen Foods'),
    ('BK', 'Bakery'),
    ('BV', 'Beverages'),
    ('CPG', 'Canned and Packaged Goods'),
    ('DG', 'Dry Goods & Grains'),
    ('SN', 'Snacks'),
    ('BR', 'Breakfast Items'),
    ('CS', 'Condiments and Sauces'),
    ('SS', 'Spices and Seasonings'),
    ('BCI', 'Baking and Cooking Ingredients'),
    ('EF', 'Ethnic Foods'),
    ('HW', 'Health & Wellness'),
    ('HC', 'Household and Cleaning'),
    ('BCC', 'Baby & Child Care'),
    ('PC', 'Personal Care'),
    ('PTC', 'Pet Care'),
    ('OTH', 'Other')
]

class Item(models.Model):
    name = models.CharField(max_length=255)  
    quantity = models.PositiveIntegerField(default=1) 
    purchased = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True) 
    category = models.CharField(
        max_length=4, 
        choices=CATEGORY_CHOICES,
        default='OTH'
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.quantity}"

    def get_full_category_name(self):
        return self.get_category_display()# this is an awesome method thanks Django !!! 

    class Meta:
        ordering = ['purchased', 'added_at']

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'item_id': self.id})
