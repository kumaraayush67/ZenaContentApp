from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Guideline(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Content(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContentVersion(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="versions")
    content_file = models.FileField()

    def __str__(self):
        return f"{self.content.name}: Version #{self.id}"


class GuidelineCheck(BaseModel):
    content_version = models.ForeignKey(ContentVersion, on_delete=models.CASCADE,
                                        related_name='guideline_checks')
    guideline = models.ForeignKey(Guideline, on_delete=models.CASCADE)
    is_passed = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = [["content_version", "guideline"]]

    def __str__(self):
        return f"{self.content_version} - {self.guideline}"
    
    @property
    def verdict(self):
        return "Pass" if self.is_passed else "Failed"
