from django.urls import path, include
from .views import FirstPageView, SignupPageView


urlpatterns=[

    
    path("",FirstPageView.as_view(),name="first_page"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("signup",SignupPageView.as_view(), name="signup"),
    

]