from django.db import models

# Create your models here.
class SubirTarea(models.Model):
    media = models.FileField(upload_to='files/', blank=True, null=True)


    def __file__(self):
        return "{0}".format(self.media)

