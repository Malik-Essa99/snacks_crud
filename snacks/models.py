from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=255, help_text='snack title')
    description = models.TextField(max_length=255,help_text="Description of the snack",default="no description available")
    purchaser = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snack_detail',args=[self.id])