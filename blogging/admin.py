from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.StackedInline):
    model = Post.category.through
    exclude = ('name', 'description',)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]
    exclude = ('category',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
