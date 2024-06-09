from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer
from .utils import analyze_resume

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        resume = self.get_object()
        summary = analyze_resume(resume.content)
        return Response({'summary': summary})
