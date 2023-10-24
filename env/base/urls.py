from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.create_room,name='create-room'),
    path('update-room/<str:pk>/',views.update_room,name='update-room'),
    path('delete-room/<str:pk>/',views.delete,name='delete-room'),
    path('login/',views.loginPage,name='loginpage'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('update-message/<str:pk>/',views.messageEdit,name='update-message'),
    path('profile/<str:pk>/',views.profile,name="profile")
    ]