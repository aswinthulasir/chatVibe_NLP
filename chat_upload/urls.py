from django.urls import path
# from rest_framework.routers import DefaultRouter

from . import views  # Assuming you have views.py in your app

urlpatterns = [
    path('chat_upload/',views.hello, name='chat_upload')
    ]
# # Create a router for automatic URL generation (optional)
# router = DefaultRouter()
# router.register('video-urls', views.VideoUrlViewSet)  # Example registration

# urlpatterns = [
#     # Include automatically generated URLs from the router
#     path('', include(router.urls)),

#     # Add additional URL patterns here if needed
#     # path('some-other-view/', views.SomeOtherView.as_view()),
# ]
