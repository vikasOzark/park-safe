from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('landing-page/', views.LandingPageView.as_view(), name="landing-page"),
    path('landing-page/<str:uuid>', views.LandingPageView.as_view(), name="landing-page"),

    ]
