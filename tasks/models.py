from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    def __str__(self):
        return self.title
