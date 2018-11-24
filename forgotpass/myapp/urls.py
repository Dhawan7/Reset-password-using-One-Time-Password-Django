from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('gotp/',views.gotp,name='gotp'),
]
