from django.urls.conf import path
from rest_framework import routers
from .views import MeasurementViewSets
from django.urls import path, include
from .views import FacebookLogin
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

router = routers.DefaultRouter()
router.register('measurements', MeasurementViewSets, 'measurements')

urlpatterns = [
     path('api/', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]
