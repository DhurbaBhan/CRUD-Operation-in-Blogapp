from django.db import models
from django import forms
from blogapp.models import BlogPost



class PostCreateForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=('post_title','post_description','slug','post_status')        