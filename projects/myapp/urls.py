from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.ProjectDetail, name="projectdetail"),
    path('description/<int:id>', views.Description, name='fulldescription'),
    path('projectadd', views.ProjectAdd, name='projectadd'),
]