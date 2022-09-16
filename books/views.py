from rest_framework import generics
from .models import *
from .serializers import *

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
