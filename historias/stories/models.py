from django.db import models

# Create your models here.
class Historia(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default = True)
    
class Fragmento(models.Model):
    id_historia = models.ForeignKey(Historia)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
