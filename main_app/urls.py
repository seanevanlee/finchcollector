# from django.contrib import admin
# # Add the include function to the import
# from django.urls import path, include
# from django.contrib import admin
from django.urls import path

from . import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     # In this case '' represents the root route
#     path('', include('main_app.urls')),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index')
]
