from django.db import models
from django.contrib.auth.models import User
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Add more fields here as needed

    def __str__(self):
        return str(self.user)

class documents(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    document_name=models.CharField(max_length=50)
    document=models.FileField(upload_to='documents', max_length=100)

    def __str__(self):
        return str(self.user)
