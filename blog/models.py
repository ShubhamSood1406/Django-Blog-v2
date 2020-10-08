from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User     # importing User model that Django provides
from django.urls import reverse     # to path redirect

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) # we didn't write .now() because we didn't want to execute now function here, but when other details are added
                                                                # auto_now fields are updated to the current timestamp every time an object is saved,
                                                                # auto_now_add field is saved as the current timestamp when a row is first added to the database.
    author = models.ForeignKey(User, on_delete= models.CASCADE) # CASCADE will delete the Post if a author is deleted
    
    def __str__(self):      # dender str method to add descriptive way to Post class(return Title), otherwise it will return an object when accessed in Shell
        return self.title

    def get_absolute_url(self):      # to redirect to path of new post created 
        return reverse('post-detail', kwargs={'pk': self.pk})