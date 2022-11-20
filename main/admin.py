from django.contrib import admin
from .models import TextBlock, Text, FeedBackRequest

# Register your models here.
@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
	list_display = ('title', )

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	pass

@admin.register(FeedBackRequest)
class FeedBackRequestAdmin(admin.ModelAdmin):
	pass
