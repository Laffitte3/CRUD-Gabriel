from django.urls import path
from .views import HomePageView,DetailPageView,CreatePageView,UpdatePageView,DeltePageView


urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("post/detail/<int:pk>",DetailPageView.as_view(),name="detail"),
    path("post/create/",CreatePageView.as_view(),name="create"),
    path("post/detail/<int:pk>/update",UpdatePageView.as_view(),name="update"),
    path("post/detail/<int:pk>/delete",DeltePageView.as_view(),name="delete"),
    

]
