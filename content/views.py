from rest_framework import viewsets, response, decorators, status

from content import serializers
from content.models import Guideline, Content, GuidelineCheck


class GuidelineView(viewsets.ModelViewSet):
    queryset = Guideline.objects.all()
    serializer_class = serializers.GuidelineSerializer


class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()\
        .prefetch_related('versions', 'versions__guideline_checks')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.ContentSerializer
        else:
            return serializers.ContentViewSerializer

    @decorators.action(detail=True, methods=['get'])
    def check_status(self, request, *args, **kwargs):
        version_id = request.query_params.get('version_id')
        
        content_version = self.get_object().versions\
            .order_by("created_at")
        
        if version_id:
            content_version = content_version.filter(id=version_id)
        
        if not content_version.exists():
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ContentVersionSerializer(instance=content_version.last())
        return response.Response(serializer.data)


class GuidelineCheckView(viewsets.ModelViewSet):
    queryset = GuidelineCheck.objects.all()
    serializer_class = serializers.GuidelineCheckSerializer
