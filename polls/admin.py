from distutils.command.register import register

from django.contrib import admin

from polls.models import Question, Choice, Post

# Register your models here.
admin.site.register([Question,Choice])


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass