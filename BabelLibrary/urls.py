"""BabelLibrary URL Configuration

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
from django.conf.urls import include, url, static
from django.contrib import admin
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
urlpatterns = [
    url(r'^', include('library.urls')),
    url(r'^reader/', include('reader.urls')),
    url(r'^dict/', include('dictionary_manager.urls')),
    url(r'^user/', include('user_manager.urls')),
    url(r'^vocabulary_manager/', include('vocabulary_manager.urls')),
    url(r'^testing_module/', include('testing_module.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': BASE_DIR}),
]

urlpatterns += static.static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static.static(STATIC_URL, document_root=STATIC_ROOT)