from click import password_option
from django.db import models
from datetime import datetime

# Create your models here.
  
class BlogPost(models.Model):
    post_title=models.CharField(max_length=200)
    post_description=models.TextField(max_length=500)
    slug=models.CharField(max_length=200)
    category_id=models.BigIntegerField(null=True)
    post_image= models.FileField(upload_to='images/post/')
    user_id=models.BigIntegerField(null=True)
    post_status=models.CharField(null=True,max_length=20) 
    created_at=models.DateTimeField(default=datetime.now(),blank=False)
    updated_at=models.DateTimeField(null=True,blank=True)
    removed_at=models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table="dhurbaapp_blogposts"