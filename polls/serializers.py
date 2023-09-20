from rest_framework.serializers import ModelSerializer
from .models import Noutbook

class NoutbookSerializer(ModelSerializer):
    class Meta:
        model = Noutbook
        fields = ('__all__')