from django.contrib import admin
from django.urls import path
from fasalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginregister, name='loginregister'),
    path('insertuser/', views.insertuser, name='insertuser'),
    path('login/', views.user_login, name='login'),
    path('success/', views.success, name='success'),
    path('logout/', views.user_logout, name='logout'),
    path('playlist/',views.playlist, name='playlist'),
    path('add-to-playlist/', views.add_to_playlist, name='add_to_playlist'),
    path('get-playlist/', views.get_playlist, name='get_playlist'),
    path('remove/', views.remove_from_playlist, name='remove_from_playlist'),
]
