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
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/',
         views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_wing/<int:wing_id>/',
         views.assoc_wing, name='assoc_wing'),
    path('wings/', views.WingList.as_view(), name='wings_index'),
    path('wings/<int:pk>/', views.WingDetail.as_view(), name='wings_detail'),
    path('wings/create/', views.WingCreate.as_view(), name='wings_create'),
    path('wings/<int:pk>/update/', views.WingUpdate.as_view(), name='wings_update'),
    path('wings/<int:pk>/delete/', views.WingDelete.as_view(), name='wings_delete'),
]
