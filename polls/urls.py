from django.urls import path
from .views import CreateView, AllApiView, UpdateStatus

urlpatterns = [
    path('create/', CreateView.as_view()),
    path('all/', AllApiView.as_view()),
    path('update_status/<int:pk>/', UpdateStatus.as_view()),
]