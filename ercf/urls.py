from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "ercf"

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('view_user/<str:pk>/', views.viewUser, name='view_user'),
    path('edit_user/<str:pk>/', views.editUser, name='edit_user'),
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:pk>', views.post, name='post'),
    path('navbar/', views.navbar, name='navbar'),
    path('form/', views.create_post, name='form'),
    path('update/<str:pk>/', views.update_post, name='update'),
    path('delete/<str:pk>/', views.delete_post, name='delete'),
    path('delete_comment/<str:pk>/', views.deleteComment, name='delete_comment'),
    path('beats/', views.beats, name='beats'),
    path('samples/', views.samples, name='samples'),
    path('create_video/', views.createVideo, name='create_video'),
    path('create_sample', views.createSample, name='create_sample'),
    path('artists', views.artists, name='artists'),
    path('music', views.music, name='music'),
    path('aboutUs', views.aboutUs, name='about_us'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)