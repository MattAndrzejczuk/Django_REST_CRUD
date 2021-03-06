from django.conf.urls import url, include
from django.contrib import admin
from cinicraft_home import views
from cinicraft_home import models
from cinicraft_home.views import *

from rest_framework import routers



# Django REST URLs:
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# Django URLs:
urlpatterns = [
    # Django
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # Django-REST
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    # Snippets:
    url(r'^snippets/', include('snippets.urls')),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]



