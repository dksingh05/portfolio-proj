from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField(max_length=1000, default='SOME STRING')
    image = models.ImageField(upload_to='images/', null=True)

