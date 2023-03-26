from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name