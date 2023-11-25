from django.urls import path
from .views import home, object_card

urlpatterns = [
    path('', home, name='home'),
    path('object_card/', object_card, name='object_card'),
]
