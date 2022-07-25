from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    # path('login/', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),

    # path('createArtist/', views.createArtist, name="artist_create"),
    # path('updateArtist<str:pk>/', views.updateArtist, name="artist_update"),
    # path('deleteArtist<str:pk>/', views.deleteArtist, name="artist_delete"),
    # path('artists/', views.artistList, name="artist_list"),

    path('artists/', views.ArtistListCreateAPIView.as_view(), name="artist_list_create"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_details"),

    
    # path('galleries/', views.GalleryList.as_view(), name="gallery_list"),
    # path('galleries/<str:pk>/', views.GalleryDetails.as_view(), name="gallery_details"),
]