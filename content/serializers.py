from rest_framework import serializers, exceptions
from content.models import Guideline, Content, ContentVersion, GuidelineCheck


class GuidelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guideline
        exclude = ()


class GuidelineCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidelineCheck
        exclude = ()


class GuidelineCheckListSerializer(serializers.ModelSerializer):
    guideline = serializers.SerializerMethodField()

    class Meta:
        model = GuidelineCheck
        fields = ('guideline', 'verdict')
    
    def get_guideline(self, obj):
        return obj.guideline.title


class ContentVersionSerializer(serializers.ModelSerializer):
    guideline_checks = GuidelineCheckListSerializer(many=True)
    content_name = serializers.SerializerMethodField()

    class Meta:
        model = ContentVersion
        fields = ('id', 'content_name', 'content_file', 'guideline_checks')
    
    def get_content_name(self, obj):
        return obj.content.name


class ContentViewSerializer(serializers.ModelSerializer):
    versions = ContentVersionSerializer(many=True)
    class Meta:
        model = Content
        fields = ('id', 'name', 'versions')


class ContentSerializer(serializers.ModelSerializer):
    content_file = serializers.FileField(required=False)
    name = serializers.CharField(required=False)

    class Meta:
        model = Content
        exclude = ()
    
    def save(self, *args, **kwargs):
        content_name = self.validated_data.get('name')
        content_file = self.validated_data.get('content_file')

        if not content_file:
            raise serializers.ValidationError("content_file is required.")

        if not self.instance:
            if not content_name:
                raise serializers.ValidationError("name is required for content creation.")
            
            content_obj = Content(name=content_name)
            content_obj.save()
        else:
            content_obj = self.instance

        content_version = ContentVersion(
            content=content_obj, content_file=content_file)
        content_version.save()
        return content_obj
