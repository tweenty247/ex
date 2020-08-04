from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('pricing.html', views.pricing, name='pricing'),
    path('blog.html', views.blog, name='blog'),
    path('blog-details.html', views.blog_details, name='blog-details'),
    # path('base.html', views.last_email, name='last_email')
]
