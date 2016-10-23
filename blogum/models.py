from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def categorize(self):
        print (self.category)
        length = len(self.category)
        phrase = []
        while length < 15:
            phrase.append(". ")
            length = length + 1
        phrase.append(self.category)
        phrase = "".join(phrase)
        return phrase