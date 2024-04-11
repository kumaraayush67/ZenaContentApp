from django.contrib import admin
from content.models import Content, Guideline, ContentVersion, GuidelineCheck

class GuidelineAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description')

class GuidelineCheckInline(admin.StackedInline):
    model = GuidelineCheck
    extra = 1
    fields = ('guideline', 'is_passed')

class ContentVersionAdmin(admin.ModelAdmin):
    list_display = ('content', 'id', 'created_at')
    list_filter = ('content', 'created_at')
    inlines = [GuidelineCheckInline]

admin.site.register(Guideline, GuidelineAdmin)
admin.site.register(ContentVersion, ContentVersionAdmin)
admin.site.register([Content, GuidelineCheck])
