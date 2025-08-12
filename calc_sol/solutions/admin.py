from django.contrib import admin
from .models import Chapter, Section, Problem, SolutionImage, Update, About, SupportResource, Feedback

# Manage stuff in admin panel.
# Register your models here.
class SolutionImageAdmin(admin.ModelAdmin):
    list_display = ('problem', 'uploaded_by', 'uploaded_at', 'status')  # Fields to display in the admin list
    readonly_fields = ('uploaded_at',)  # Fields that should be readonly in the form
    list_filter = ('status',)  # Optionally, filter by status in the admin interface

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('get_chapter_section', 'problem_number', 'description')
    ordering = ('section__chapter__number', 'section__number', 'problem_number')  # ✅ This will sort correctly

    def get_chapter_section(self, obj):
        return f"{obj.section.chapter.number}.{obj.section.number}"
    get_chapter_section.short_description = 'Chapter.Section'

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title',)

@admin.register(SupportResource)
class SupportResourceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'submitted_at')

# Register Models here
admin.site.register(About, AboutAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(SolutionImage, SolutionImageAdmin)
admin.site.register(Chapter)
admin.site.register(Section)
# admin.site.register(Problem)


