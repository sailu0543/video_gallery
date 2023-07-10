# Define the serializer for the video model using the rest framework
from rest_framework  import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'file', 'thumbnail')
        