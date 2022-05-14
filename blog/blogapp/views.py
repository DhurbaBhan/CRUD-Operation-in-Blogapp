import email
from django.shortcuts import render
from blogapp.forms import PostCreateForm
from blogapp.models import BlogPost


# Create your views here.

def post_create(request):
    template='posts/create.html'
    post_form=PostCreateForm
    context={'form':post_form}
    if request.method=='POST':
        obj_post=BlogPost()
        obj_post.post_title=request.POST.get('post_title')
        obj_post.post_description=request.POST.get('post_description')
        obj_post.slug=request.POST.get('slug')
        obj_post.post_status=request.POST.get('post_status')
        obj_post.save()
        context.setdefault('message','Your post created Successfully')
        
        return render (request,template,context)

    else:
        return render (request,template,context)

def post_index(request):
    template='posts/index.html'
    posts=BlogPost.objects.all()
    context={'posts':posts}
    return render(request,template,context)

def post_edit(request,post_id):
    template='posts/edit.html'
    post=BlogPost.objects.get(id=post_id)
    context={'post':post}
    return render(request,template,context)

def post_show(request,post_id):
    template='posts/show.html'
    post=BlogPost.objects.get(id=post_id)
    context={'post':post}
    return render(request,template,context)

def post_update(request):
    template='posts/index.html'
    post_form=PostCreateForm
    posts=BlogPost.objects.all()
    context={'form':post_form,'posts':posts}
    
    if request.method=='POST':
        obj_post=BlogPost.objects.get(id=request.POST.get('post_id'))
        obj_post.post_title=request.POST.get('post_title')
        obj_post.post_description=request.POST.get('post_description')
        obj_post.slug=request.POST.get('slug')
        obj_post.post_status=request.POST.get('post_status')
        obj_post.save()
        

        return render(request,template,context)

    else:
        return render(request,template,context)  

def post_delete(request,post_id):
    template='posts/index.html'
    post=BlogPost.objects.get(id=post_id)
    post.delete()
    posts=BlogPost.objects.all()
    context={'posts':posts}
    return render(request,template,context)    

