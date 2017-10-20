from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CoinlistViewSet, DetailsViewSet

router = routers.SimpleRouter()

router.register(r'list', CoinlistViewSet)
router.register(r'details', DetailsViewSet)
urlpatterns = {
    url(r'', include(router.urls))
    # url(r'^api/(?P<pk>[0-9]+)/$', Details.as_view(), name="details"),
}
urlpatterns = format_suffix_patterns(urlpatterns)
