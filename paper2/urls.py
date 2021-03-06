"""paper2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from first_app import views
from chat import views
# from chat import views
# from accounts import views
from django.contrib import admin
urlpatterns = [

    # url(r'^$',views.index,name='home'),
    url(r'^home/',include('first_app.urls', namespace='first_app')),
    url(r'^',include('first_app.urls')),
    url(r'^chat/',include('chat.urls')),

    # url(r'^accounts/',include('accounts.urls')),

    # url(r'^admin/', admin.site.urls),
    # url(r'^users/', include(('accounts.urls','accounts'), namespace='users')),
    # url(r'^accounts/', include('accounts.urls')),


    # url(r'^logout$',views.user_logout,name='logout'),
    # url(r'special/',views.special,name='special'),
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
