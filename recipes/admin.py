from django.contrib import admin
from.models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Post) # para registar esta tem que ser metida em cima da class
class PostAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

