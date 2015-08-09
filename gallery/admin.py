from django.contrib import admin

# Register your models here.

from .models import ImageGallery

class GalleryAdmin(admin.ModelAdmin):
	fields 			= ['image_name','image_url']
	list_display 	= ('image_name','image_url')
	#list_filter 	= ['image_name']
	search_fields	= ['image_name']

admin.site.register(ImageGallery, GalleryAdmin)