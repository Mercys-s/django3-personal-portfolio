from django.db import models


class Blogs(models.Model):
    title = models.CharField (max_length = 100)
    description = models.TextField ()
    date = models.DateField (auto_created=True)

    def __str__(self):
        return self.title

