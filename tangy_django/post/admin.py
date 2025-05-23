from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):  
    model = PostImage
    extra = 1  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'content')  
    prepopulated_fields = {'slug': ('title',)}  
    inlines = [PostImageInline]  


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'caption') 
    search_fields = ('caption',)
