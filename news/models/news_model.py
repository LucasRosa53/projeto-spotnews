from django.db import models
from models.user_model import Users
from models.category_model import Categories


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )
    created_at = models.DateField()
    image = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True
    )
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
