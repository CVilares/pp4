from . import views
from django.urls import path


urlpatterns = [
    # Set IntroView as the root URL view
    path('', views.IntroView.as_view(), name='intro'),
    # Optional, in case you want to support '/intro/'
    # The home view, if needed
    path('home/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
