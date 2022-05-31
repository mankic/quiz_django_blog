from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    # category에는 Category object가 들어가야한다.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




