from django.urls import path

from dwitter import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>/", views.profile_views, name="profile"),

]
