from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedImage
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadedImageSerializer
from .utils import predict_value

model_path = 'All_images.pkl'

class UploadImageView(APIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            uploaded_image = serializer.save()
            image_path = uploaded_image.image.name
            prediction = predict_value(model_path, image_path)
            print(prediction)
            uploaded_image.predict_value = prediction
            uploaded_image.save()
            return Response({'prediction': prediction}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)