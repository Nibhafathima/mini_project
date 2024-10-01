from django.urls import path
from temp import views
urlpatterns=[
    path('home/',views.home),
    path('admin_home/',views.admin_home),
    path('user_home/',views.user_home),
    path('driver_home/',views.driver_home), 
    path('dashboard/',views.dashboard), 
]
