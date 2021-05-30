from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from . serializers import MailSerailizer, RatingSerializer
# from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework.views import APIView
from . models import Mail, Rating
from rest_framework import status, viewsets
from rest_framework.response import Response


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerailizer
    lookup_field = 'id'

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = 'id'

    def list(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        if ratings:
            sum = 0.0
            for rating in ratings:
                sum += rating.rate
            computed_rating = round((sum / ratings.count()), 2)
        else:
            computed_rating = 0
        dict = {
            "ratings":serializer.data,
            "rating_computed":computed_rating
        }
        return Response(dict)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

# class AddRating(CreateAPIView):
#     serializer_class = RatingSerializer
#     permission_classes = [AllowAny]

# class RatingsList(ListAPIView):
#     serializer_class = RatingSerializer
#     permission_classes = [IsAdminUser]
#     queryset = Rating.objects.all()

# class MessagesList(ListAPIView):
#     serializer_class = MailSerailizer
#     permission_classes = [IsAdminUser]
#     queryset = Mail.objects.all()


