from django.db import models

# Create your models here.

class FecturedBanner(models.Model):
    name = models.CharField(max_length=255)
    banner_image = models.ImageField(upload_to='banner/')
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.created_at})"