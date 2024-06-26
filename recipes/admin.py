from django.contrib import admin
from.models import Category, Post, Speciality


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

    # Register your models here.
class SpecialityAdmin(admin.ModelAdmin):
    ...

@admin.register(Post) # para registar esta tem que ser metida em cima da class
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'created_at', 'is_published']
    list_display_links = ['title',]
    search_fields = ['id', 'title','description',] #'speciality' 
    list_filter = ['category', 'author', 'is_published']
    list_per_page = 10
    list_editable = ['is_published',]
    ordering = ['-id']
    prepopulated_fields = {
        "slug": ('title',)
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Speciality, SpecialityAdmin)

