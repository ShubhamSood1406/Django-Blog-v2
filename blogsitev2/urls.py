"""blogsitev2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # to include urls of Blog App
from users import views as user_views    # to include views of User App
from django.contrib.auth import views as auth_views # to include django built-in views to login and logout
from django.conf import settings        # for serve media file on web
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),    # to use register route of users App
    path('profile/', user_views.profile, name='profile'),    # to use profile route of users  App
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),     # login & logout path from Django built-in views
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/', include('blog.urls')),    # url of blog App in the project
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # to add Media_Url and Media_Root to current urlpatterns
