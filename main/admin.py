from django.contrib import admin
from .models import TextBlock, Text, FeedBackRequest, DubaiVisaRequest

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

@admin.register(DubaiVisaRequest)
class DubaiVisaRequestAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'created', 'passport_registered_at', 'now_located_in')
	search_fields = (
		'passport_registered_at',
		'now_located_in',
		'first_name',
		'last_name',
		'passpost_series',
		'passport_closure_date',
		'created',
		'updated'
	)
