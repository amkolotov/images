from django.urls import path

from . import views

app_name = 'apps.main'

urlpatterns = [
    path('images/', views.ImageViewSet.as_view({'get': 'list'}), name='images'),
    path('images/<int:pk>/', views.ImageViewSet.as_view({'get': 'retrieve'}), name='image'),
    path('images/save/', views.ImageViewSet.as_view({'post': 'create'}), name='save_image'),
]
