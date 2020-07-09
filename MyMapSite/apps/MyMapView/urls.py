from django.urls import path

from . import views

app_name = 'MyMapView'
urlpatterns = [
    path('', views.maine, name='maine'),
    path('news/', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('contacts/', views.contacts, name='contacts'),
    path('<int:showcode_id>/', views.detail, name='detail'),
    path('<int:showcode_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('gallery/<int:image_id>/', views.detail_img, name='detail_img'),
    path('gallery/<int:image_id>/leave_comment/', views.leave_imgcomment, name='leave_imgcomment'),
]