from django.db import models

# Create your models here.

class Aa(models.Model):
    date = models.DateField(auto_now_add=True)
    National_code = models.IntegerField()
    first_name = models.CharField(("first name"),max_length=100)
    last_name = models.CharField(('last name'),max_length=100)
    

    
    def __str__(self): 
        return str(self.pk)

