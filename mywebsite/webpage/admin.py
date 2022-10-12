from django.contrib import admin


# Register your models here.
from.models import blog,post,Contact
admin.site.register(blog)
admin.site.register(post)
admin.site.register(Contact)