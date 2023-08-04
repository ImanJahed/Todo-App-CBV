from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from todo.models import Todo


class TodoListApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]




class TodoRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer