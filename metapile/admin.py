from django.contrib import admin

from metapile.models import Photo

@admin.register(Photo)
class PhotoAdmin (admin.ModelAdmin):
  list_display = ['path', 'bucket', 'tag_count']
  
  def tag_count (self, obj):
    if obj.metadata:
      return len(obj.metadata.keys())
      
    return 0
    