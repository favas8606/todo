from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name="start"),
    # path('details', views.details, name="details"),
    path('delete/<int:id>/', views.done, name = "delete"),
    path('edit/<int:id>/',views.update, name="update"),
    path('index', views.TaskListView.as_view(), name='index'),
    path('cdetail/<int:pk>/', views.TaskDetailView.as_view(), name="cdetail"),
    path('cupdate/<int:pk>/', views.TaskUpdateView.as_view(), name="cupdate"),
    path('cdelete/<int:pk>/', views.TaskDeleteView.as_view(),name="cdelete")
    

]