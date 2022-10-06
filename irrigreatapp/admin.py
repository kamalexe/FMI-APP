from django.contrib import admin
from .models import SmUser,SmUserProfile,Post,Comment
# Register your models here.
admin.site.register(SmUser)
admin.site.register(SmUserProfile)
admin.site.register(Post)
admin.site.register(Comment)
