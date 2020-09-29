from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField(max_length=1000, default='SOME STRING')
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')