from django.urls import path

from movies import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<pk>', views.DirectorDetailView.as_view(), name='director_detail'),
    path('movie/<pk>', views.MovieDetailView.as_view(), name='movie_detail')
]
