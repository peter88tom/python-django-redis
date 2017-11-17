from django.conf.urls import url,include
from redisapp import views

urlpatterns =[
  url(r'^$', views.HomePageView, name="index")
]
