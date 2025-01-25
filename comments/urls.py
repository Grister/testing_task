from django.urls import path
from comments import views

app_name = 'comments'


urlpatterns = [
    path('', views.PostView.as_view(), name='short_index'),
    path('blog/', views.PostView.as_view(), name='index'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
]
