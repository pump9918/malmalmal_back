from rest_framework import viewsets

from users.models import Profile, EditorProfile
from .models import Post, Editor_Post   
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer, EditorPostSerializer, EditorPostCreateSerializer 


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)  
        serializer.save(author=self.request.user, profile=profile)
    
        
        
class EditorPostViewSet(viewsets.ModelViewSet):
    queryset = Editor_Post.objects.all()
    permission_classes = [CustomReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EditorPostSerializer
        return EditorPostCreateSerializer
    
    def perform_create(self, serializer):
        editor_profile = EditorProfile.objects.get(user=self.request.user)  
        serializer.save(author=self.request.user, editor_profile=editor_profile)
        