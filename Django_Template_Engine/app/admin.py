from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.
class PublisherAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'country','website')

class AuthorAdminView(admin.ModelAdmin):
    list_display = ('id','name','email')

class BookAdminView(admin.ModelAdmin):
    list_display = ('id','title','authors','publisher','publication_date')

    def authors(self, obj):
        return obj.authors.name
    authors.short_description = 'Authors'


admin.site.register(Publisher, PublisherAdminView)
admin.site.register(Author, AuthorAdminView)
admin.site.register(Book, BookAdminView)

