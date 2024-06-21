from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer
from api.register.models import Person

class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.none()

    def post(self, request, user_id):
        try:
            user = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.is_logged_in:
                return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['user'] = user.id
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response({'message': 'Notification successful'}, status=status.HTTP_200_OK)


class NotificationDeleteView(APIView):
    def delete(self, request, user_id, notification_id, format=None):
        
        try:
            user = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_logged_in:
                return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            notification = Notification.objects.get(id=notification_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            notification = Notification.objects.get(id=notification_id, user_id=user_id)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not created by this user."}, status=status.HTTP_404_NOT_FOUND)
        

        notification.delete()
        notifications = Notification.objects.filter(user_id=user_id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        try:
            user = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_logged_in:
            return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Notification.objects.filter(user_id=user_id)
