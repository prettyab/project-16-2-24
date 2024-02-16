from django.urls import path
from.import views


urlpatterns = [
    path('',views.homee_view,name='homee_view'),
    path('register_view/',views.register_view,name='register_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('home2/', views.home2, name='home2'),

    # Add other URL patterns as needed
]
