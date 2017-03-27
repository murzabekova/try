"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from homepage import views as homepage_views
from post import views as post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage_views.posts, name='home'),
    url(r'^all/$', post_views.show_all_posts, name='all_posts')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
