from django.contrib import admin
from .models import Student, Video
from .models import Category, Book, BookSearch
from embed_video.admin import AdminVideoMixin
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Student)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookSearch)
admin.site.register(Video, AdminVideo)
