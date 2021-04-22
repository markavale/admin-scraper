from django.urls import path, include
from . views import  MessagesViewSet, RatingViewSet#AddRating, RatingsList, MessagesList, 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('messages', MessagesViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('send-mail/', CreateMail.as_view(), name='send-mail'),
    # path('add-rating/', AddRating.as_view(), name='create-rating'),
    # path('ratings/', RatingsList.as_view(), name='ratings'),
    # path('messages/', MessagesList.as_view(), name='messages'),
]
