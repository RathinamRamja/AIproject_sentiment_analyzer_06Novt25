from django.urls import path
from . import views
# from .views import Sentiment

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze_sentiment, name='analyze_sentiment'),
    
    # path("sentiment/",Sentiment.as_view()),
]