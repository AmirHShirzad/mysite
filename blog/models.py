from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.


class Post(models.Model):
    # image
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    # order items in general with Meta class not just showing in admin panel
    # and using class PostAdmin(admin.ModelAdmin):ordering = ['created_date'] in admin.py
    class Meta:
        ordering = ['-published_date']

    # change post name from id to title
    def __str__(self):
        return "{} - {}" .format(self.id, self.title)
