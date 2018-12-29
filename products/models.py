from django.db import models
from django.contrib.auth.models import User
import textwrap
# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=200)
	url = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	votes_total = models.BigIntegerField(default=0)
	image = models.ImageField(upload_to='images/%Y/%m/%d/')
	icon = models.ImageField(upload_to='icons/%Y/%m/%d/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	def pub_date_pretty(self):
		return self.pub_date.strftime("%d %B %Y")

	def summary(self):
		return textwrap.shorten(self.body, width=100, placeholder="...")

	def __str__(self):
		return self.title