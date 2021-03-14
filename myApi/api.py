from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView

class TaskList(APIView):
    def get(self, request):
        model = MyTaskList.objects.all()
        serializer = TaskSerializers(model, many=True)
        return Response (serializer.data)