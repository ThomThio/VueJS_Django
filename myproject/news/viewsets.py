from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
class NewsPageViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer