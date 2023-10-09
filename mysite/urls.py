"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
import debug_toolbar  
from django.contrib.auth import views as auth_views

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path ('url address, 'view', 'name', ... )
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),

    path('accounts/', include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', include('robots.urls')),
    path("__debug__/", include(debug_toolbar.urls)),
    path('captcha/', include('captcha.urls')),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# static ('static', 'base / static')
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)