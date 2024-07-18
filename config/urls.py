
from django.contrib import admin
from django.urls import path
from .views import first_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
]
