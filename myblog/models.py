from django.db import models
from django.utils import timezone
# Create your models here.
class post  (models.Model):
    postDate = models.DateTimeField(default = timezone.now)
    postTitle = models.CharField(max_length=50)
    postContent = models.TextField()
    postNote = models.TextField()
    objects = models.Manager()  # required

    class Meta:
        ordering = ('postDate',)
    def __str__(self):
        return self.postTitle