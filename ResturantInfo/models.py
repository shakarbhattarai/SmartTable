from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class ResturantInfo(models.Model):
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ResturantName = models.CharField(max_length=100, blank=True, default='')
    OwnerName = models.CharField(max_length=100, blank=True, default='')
    District=models.CharField(max_length=50, blank=True, default='Kathmandu')
    Address=models.CharField(max_length=50, blank=True, default='Baneshwor')
    Trial = models.BooleanField(default=True)

    class Meta:
        ordering = ('CreatedAt',)