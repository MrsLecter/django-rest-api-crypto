from posixpath import basename
from django.contrib import admin
from django.urls import path, include, re_path
from currency.views import CurrencyViewSet, MarketView

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'currency', CurrencyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/market/<str:market>', MarketView.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
