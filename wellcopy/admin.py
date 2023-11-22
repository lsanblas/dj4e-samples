from django.contrib import admin

# Register your models here.

from wellcopy.models import Postcopy, Brand, Guitar, Review, Comment

admin.site.register(Postcopy)
admin.site.register(Brand)
admin.site.register(Guitar)
admin.site.register(Review)
admin.site.register(Comment)
