from django.db import models

class Rule(models.Model):
    query = models.CharField(max_length=255)

    def __str__(self):
        return self.query
