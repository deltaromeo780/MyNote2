from django.contrib import admin
from .models import Tag, Note  # 4

# Register your models here.
admin.site.register(Tag)  # 4
admin.site.register(Note)  # 4
# 5 templates/noteapp, index.html
