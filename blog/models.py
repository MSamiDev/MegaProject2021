from django.db import models
from django.utils.timezone import now 

# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField
    title = models.CharField(max_length=300)
    blog_slug = models.SlugField(max_length=300, editable=True, unique=True)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    discription = models.CharField(max_length=700)
    content = models.TextField()
    publish_date = models.DateTimeField(default=now())
    cover_image = models.ImageField(upload_to="blog/cover_images", default="")
    autor = models.CharField(max_length=100)