from django.urls import path, include
from . import views

urlpatterns =[
    path("", views.projects, name="projects"),
    path("project/", views.project, name="project"),
    path("project-obj/<str:pk>/", views.project, name="project" ),
    path("create-project/", views.createProject, name='create-project'),
    path("update-project/<str:pk>/", views.updateProject, name="update-project"),
    path("delete-project/<str:pk>/", views.deleteProject, name="delete-project"),
    path('users/', include('users.urls')),

    
]