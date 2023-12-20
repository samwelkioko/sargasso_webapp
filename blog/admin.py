from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
admin.site.site_header = "Sargasso Admin"
admin.site.site_title = "sargasso Admin Portal"
admin.site.index_title = "Welcome to Sargasso Reclamation Portal"