from django.urls import path
from .views import NewsPost, NewsID

urlpatterns = [
    path('', NewsPost.as_view()),
    path('<int:pk>', NewsID.as_view()),

]