from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	"""docstring for Category"""
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
	title = models.CharField(max_length = 45)
	slug = models.SlugField(max_length = 45)

	def __unicode__(self):
		return '%s' % self.title

class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length = 45)
	date = models.DateTimeField(auto_now = True)
	content = models.TextField(null = True)
	category = models.ForeignKey(Category, null = True)

	def __unicode__(self):
		return '%s' % self.title


		
