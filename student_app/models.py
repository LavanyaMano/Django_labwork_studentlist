from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class StudentDetail(models.Model):

    name = models.CharField(max_length = 200)
    published = models.DateTimeField(null=True,blank=True)
    bio =models.TextField(blank=True)
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_app:detail",kwargs={"id":self.pk})
