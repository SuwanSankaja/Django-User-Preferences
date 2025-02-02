from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    notification_preference = models.BooleanField(default=False)
    email_frequency = models.CharField(max_length=10, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], blank=True, null=True)
    profile_visibility = models.CharField(max_length=10, choices=[('private', 'Private'), ('public', 'Public')], default='private')
    data_sharing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)