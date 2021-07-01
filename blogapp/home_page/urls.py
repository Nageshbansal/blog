from django.urls import path
from . import views
from .models import Post
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('',views.index,name='index'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("<int:id>",views.posts,name='posts'),
    path("dashboard",views.dashboard, name="dashboard"),
    path("add_post" ,views.add_post, name="add_post"),
    path("addcomment/<int:id>/", views.addcomment, name="addcomment"),
    
    path("edit_post/<int:id>/", views.edit_post, name="edit_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
    path("profile",views.profile,name="profile"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

