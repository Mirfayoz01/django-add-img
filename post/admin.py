from django.contrib import admin
from .models import Post
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'images']

    def images(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):  # photo mavjudligini tekshirish
            return format_html(
                f'''<a href="{obj.photo.url}" target="_blank">
                            <img src="{obj.photo.url}" alt="image" width="150" height="100" 
                                 style="object-fit: cover;"/>
                        </a>'''
            )
        return "No Image"  # Agar fayl bo'lmasa, xatolik chiqarish o'rniga bu matnni qaytaramiz
    images.short_description = "Image Preview"

    def img(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):  # photo mavjudligini tekshirish
            return format_html(
                f'''<a href="{obj.photo.url}" target="_blank">
                              <img src="{obj.photo.url}" alt="image" width="150" height="100"
                                   style="object-fit: cover;"/>
                          </a>'''
            )
        return "No Image"
    img.short_description = "Clickable Image"
