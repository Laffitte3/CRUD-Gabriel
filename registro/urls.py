from django.urls import path, include
from .views import FirstPageView, SignupPageView, LogoutPageView


urlpatterns=[

    
    path("",FirstPageView.as_view(),name="first_page"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("sign up",SignupPageView.as_view(), name="signup"),
    path("logout1",LogoutPageView.as_view(),name="logout1"),
    

]