from django.contrib import admin
from .models import TextBlock, Text, FeedBackRequest

# Register your models here.
@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
	list_display = ('title', )

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	search_fields = ('text', )	


@admin.register(FeedBackRequest)
class FeedBackRequestAdmin(admin.ModelAdmin):
	list_display = ('from_page', 'created', 'email', 'name')
	list_filter = ('done', 'from_page')

	search_fields = ('email', 'additional_message', 'name', 'phone')	
	ordering = ('-created', 'done')
