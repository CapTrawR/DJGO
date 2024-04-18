from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name # isto em admin em vez de mostrar a categoria object 1 vai mostrar o nome que metemos la



class Post(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    post_field = models.TextField(max_length=3000)
    post_field_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m%d/', blank = True, default = '' ) # aqui nao precisa de ter imagem acossiada
    category = models.ForeignKey(
        Category, on_delete = models.SET_NULL, null=True
    )
    def __str__(self):
        return self.title # admin em vez de mostrar a categoria object 1 vai mostrar o title
    
    author = models.ForeignKey(
        User, on_delete = models.SET_NULL, null=True
    )


