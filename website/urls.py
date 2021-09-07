from django.urls import path
from website.views import Home_view, Contact_view, About_us_view

urlpatterns = [
    path('', Home_view),
    path('contact/', Contact_view),
    path('about/', About_us_view)
]