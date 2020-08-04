from django.db import models


# from django.db import models

class UserInfo(models.Model):
    blog_title = models.CharField(max_length=100)
    blog = models.CharField(max_length=100, blank=True)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # dob = models.DateField()

    # bio = models.TextField(max_length=200)


    def __str__(self):
        return self.email