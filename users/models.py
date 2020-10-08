from django.db import models
from django.contrib.auth.models import User     # importing User model that Django provides
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)    # OneToOne denotes that one User - one Profile, CASCADE will delete the Profile if User is deleted
    image = models.ImageField(default='default.png', upload_to='profile_pics')      # upload_to, directory where image will be saved

    def __str__(self):      # dender str method to add descriptive way to Profile class(return Username), otherwise it will return an object when accessed in Shell
        return ('{} Profile'.format(self.user.username))

    # to override Form save() method and reduce the image size and then save it
    def save(self):
        super().save()      # inherit the parent properties

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)