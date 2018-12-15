from django.db import models

class UserInformations(models.Model):
    login_user = models.CharField(max_length = 15)
    email_user = models.EmailField()

    def __str__(self):
        return self.login_user
