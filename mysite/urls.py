"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from polls import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^home/$', views.homeview),
	url(r'^ep-1/$', TemplateView.as_view(template_name='ep-1.html')),
	url(r'^ep-2/$', TemplateView.as_view(template_name='ep-2.html')),
	url(r'^ep-3/$', TemplateView.as_view(template_name='ep-3.html')),
	url(r'^ep-4/$', TemplateView.as_view(template_name='ep-4.html')),
]
