"""my_virtual_thoughts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
''' These URL Patterens are used to link urls to views, it will be useful if you create the views first and the linke the urls to the views. 

'''
from django.urls import path
from .views import Homepage,EntryView,CreatePost
urlpatterns = [
	path('', Homepage.as_view(),name="blog-home"),
	path('entry/<int:pk>/' , EntryView.as_view(), name="entry-detail"),
	path('create_post/',CreatePost.as_view(success_url="/"),name='create-post')
]
