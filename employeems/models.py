from django.db import models
from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    # Additional fields for the Admin model
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.username  # Return the username as a string representation

    class Meta:
        db_table = 'admin'  # Set the database table name (optional)
