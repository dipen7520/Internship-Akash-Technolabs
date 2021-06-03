from django.urls import path,include
from . import views
urlpatterns = [
    path('Day_7',views.world,name="hello india")
]