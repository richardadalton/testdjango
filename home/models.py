from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        status = "done" if self.done else "not done"
        return "{0} ({1})".format(self.name, status)