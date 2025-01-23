from django.urls import path
from comments import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='short_index'),
    path('blog/', views.TaskListView.as_view(), name='index'),
    # path('create/', views.TaskListView.as_view(), name='create'),
    # path('<id:id>/', views.TaskListView.as_view(), name='detail'),
    # path('<id:id>/delete/', views.TaskListView.as_view(), name='delete'),
]
