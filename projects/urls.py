from django.urls import path
from projects import views
app_name = "projects"
urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("<int:k>", views.project_detail, name="project_detail"),
    path("about_me", views.about_me, name="about_me"),
    path("blog", views.blog, name="blog")
]