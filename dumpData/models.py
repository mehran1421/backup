from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    title=models.CharField(max_length=200)
    thumbnail=models.ImageField(upload_to='images')
    category = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
