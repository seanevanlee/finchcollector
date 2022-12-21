# from django.contrib import admin
# # Add the include function to the import
# from django.urls import path, include
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # In this case '' represents the root route
    path('', include('main_app.urls')),
]
