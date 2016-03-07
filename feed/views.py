from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(updated__lte=timezone.now()).order_by('updated')
    return render(request, 'feed/post_list.html', {'posts': posts})

# Create your views here.
