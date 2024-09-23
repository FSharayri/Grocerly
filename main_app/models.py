from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  
    quantity = models.PositiveIntegerField(default=1) 
    purchased = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True) 
    category = models.CharField(max_length=100) # might change it later 

    def __str__(self):
        return f"{self.name} - {self.quantity}"

    class Meta:
        ordering = ['purchased', 'added_at']

# grocery_categories = [
#     "Fresh Produce",
#     "Dairy",
#     "Meat and Poultry",
#     "Seafood",
#     "Frozen Foods",
#     "Bakery",
#     "Beverages",
#     "Canned and Packaged Goods",
#     "Dry Goods & Grains",
#     "Snacks",
#     "Breakfast Items",
#     "Condiments and Sauces",
#     "Spices and Seasonings",
#     "Baking and Cooking Ingredients",
#     "Ethnic Foods",
#     "Health & Wellness",
#     "Household and Cleaning",
#     "Baby & Child Care",
#     "Personal Care",
#     "Pet Care"
# ]