from django.shortcuts import render
from post.models import Post, Category
import datetime
# Create your views here.


def show_all_posts(request):
	news = {
		'posts': Post.objects.all().order_by('-date'),
		#'message': 'first page',
		#'name': 'Home',
	}
	return render(request, 'post/all.html', news)

