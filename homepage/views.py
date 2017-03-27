from django.shortcuts import render
from post.models import Post
import datetime

# Create your views here.

def posts(request):
    context = {
        'context': Post.objects.all().order_by('-date'),
        'message': 'first page',
    }
    return render(request, 'homepage/all.html', context)