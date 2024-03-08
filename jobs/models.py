from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)

    # Another way of showing more information about the object in admin panel
    # def __str__(self):
    #     return self.summary