from django.conf.urls import url, include
from rest_framework import routers

from .views import UsersViewSet



router = routers.SimpleRouter()
router.register(r'', UsersViewSet)
urlpatterns = router.urls