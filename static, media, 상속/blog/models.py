from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=20)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.title
