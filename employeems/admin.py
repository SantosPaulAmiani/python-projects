from django.db import models

class Admin(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store password securely (use Django's authentication system for user authentication)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username  # Return the username as a string representation

    class Meta:
        db_table = 'admin'  # Set the database table name (optional)

# Additional settings can be added, such as custom methods for user authentication.
