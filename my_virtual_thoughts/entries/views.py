from django.shortcuts import render

from .models import Entry
# Create your views here.
from django.views.generic import ListView,DetailView ,CreateView


class Homepage(ListView):
	model=Entry
	template_name='index.html'
	context_object_name="blog_entries"
	ordering=['-entry_date']
	paginate_by=3

class EntryView(DetailView):
	model=Entry
	template_name='detailed.html'

class CreatePost(CreateView):
	model=Entry
	template_name='create_post.html'
	fields=['entry_title','entry_text', 'entry_image']

	def form_valid(self,form):
		form.instance.entry_author=self.request.user	
		return super().form_valid(form)
