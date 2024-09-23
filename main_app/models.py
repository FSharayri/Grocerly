from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  
    quantity = models.PositiveIntegerField(default=1) 
    purchased = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.quantity}"

    class Meta:
        ordering = ['purchased', 'added_at']
