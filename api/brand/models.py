from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="brandLogo/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name