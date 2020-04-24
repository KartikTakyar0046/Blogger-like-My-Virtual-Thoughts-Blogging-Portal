from django.db import models
from django.contrib.auth.models import User		
# Create your models here.
class Entry(models.Model):
	entry_title=models.CharField(max_length=100)
	entry_text=models.TextField(max_length=100000)
	entry_date=models.DateTimeField(auto_now_add=True)
	entry_author=models.ForeignKey(User, on_delete=models.CASCADE)
	entry_image = models.ImageField(upload_to='images/')


	class Meta:
		verbose_name_plural="entries"

	def __str__(self):
			return f'{self.entry_title}'