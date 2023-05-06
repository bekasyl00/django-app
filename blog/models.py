
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    long_link = models.URLField(verbose_name="Длинная ссылка", max_length=250)
    short_link = models.CharField(verbose_name="Сокращенная ссылка", max_length=250, unique=True)
    date=models.DateTimeField('дата',default=timezone.now)
    def __str__(self):
        return self.short_link
    
    def get_absolute_url(self):
        return reverse('url', kwargs={'slug': self.short_link})
    class Meta:
        verbose_name='sslka'
        verbose_name_plural='sslka'
    
    
    
    
    
    
    
    
    
 