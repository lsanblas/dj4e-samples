from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Postcopy(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='postcopy_owner')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

class Brand(models.Model) :
    name = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )
    description = models.TextField()
    url = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(2, "Url must be greater than 2 characters")]
    )
    
    # Picture
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True, 
                                    help_text='The MIMEType of the file')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='brand_owner')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.name
    
class Guitar(models.Model) :
    name = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )
    specs = models.TextField()
    
    # Picture
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True, 
                                    help_text='The MIMEType of the file')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='guitar_owner')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.name
    
class Review(models.Model) :
    content = models.TextField()
    score = models.FloatField()
    likes = models.IntegerField(null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='review_owner')
    guitar = models.ForeignKey('Guitar', on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model) :
    content = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='comment_owner')
    review = models.ForeignKey('Review', on_delete=models.CASCADE, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.content) < 15 : return self.content
        return self.content[:11] + ' ...'