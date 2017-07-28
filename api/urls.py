from django.conf.urls import url
from rest_framework import routers

from api.views import videos

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'videos', videos.VideoViewSet, base_name="videos")
urlpatterns = urlpatterns + router.urls