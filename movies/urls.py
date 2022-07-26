
from django.conf.urls.static import static
from django.http import Http404
from django.urls import path
from . import views
from django_movies import settings
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('movie/<slug:slug>/', views.MovieView.as_view(), name='movie'),
    path('addmovie/', views.AddView.as_view(), name='addmovie'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.Logout, name='logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('movie-edit/<int:pk>/', views.post_edit, name='post_edit'),

    #ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status'),
    path('update_movie_redact/<int:pk>/<slug:type>', views.update_movie_redact, name='update_movie_redact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

