from django.conf.urls import include
from django.urls import path , include
from town import views
from rest_framework import DefaultRouter

# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')





urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # path('', include(router.urls))
]