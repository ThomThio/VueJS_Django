from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    time_checked = models.DateTimeField()
    website = models.TextField()
    html_content = models.TextField()