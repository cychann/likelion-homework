from django.db import models

# Create your models here.


class Blog(models.Model):
    HOW_FEEL = (
        ('B', 'Bad'),
        ('H', 'Happy'),
        ('S', 'Soso'),
    )
    mood = models.TextField(
        choices=HOW_FEEL,
        help_text='Select your mood',
        default='S',
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
