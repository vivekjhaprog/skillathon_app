from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import User

# Create your models here.
class Article(models.Model):
	
	"""docstring for Article"models.Modelf 
	__init__(self, arg):
		super(Article,models.Model._
		_init__()
		self.arg = arg"""
	title=models.CharField(max_length=250)
	content=models.TextField(max_length=5000)
	posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
	posted_on=models.DateTimeField(auto_now_add=True)