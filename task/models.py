from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
