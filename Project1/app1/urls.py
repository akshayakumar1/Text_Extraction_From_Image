from django.urls import path
from .views import img_data

urlpatterns = [
    path('image/',img_data),
]