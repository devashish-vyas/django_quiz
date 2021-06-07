from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home-page'),
    path('register/',views.register,name='register-page'),
    path('quiz/',views.quizoption , name='quizoption')
] 
