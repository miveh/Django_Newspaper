# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    # level 2
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('', HomePageView.as_view(), name='home'),
]
