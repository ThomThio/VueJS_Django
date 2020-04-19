from rest_framework import routers
from article.viewsets import ArticleViewSet
from news.viewsets import NewsPageViewSet
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
router.register('news', NewsPageViewSet)