from django.db import models

# Create your models here.
class test(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    extra = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()


    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]