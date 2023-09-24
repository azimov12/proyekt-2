from django.urls import path
from .views import CreateView, AllApiView, DetaildestroyUpdateView

urlpatterns = [
    path('create/', CreateView.as_view()),
    path('all/', AllApiView.as_view()),
    path('<int:pk>/', DetaildestroyUpdateView.as_view()),
]