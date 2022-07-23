from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    # path('login/', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),

    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/<int:pk>/', views.ArtistDetails.as_view(), name="artist_details"),
    
    path('galleries/', views.GalleryList.as_view(), name="gallery_list"),
    path('galleries/<str:pk>/', views.GalleryDetails.as_view(), name="gallery_details"),
]