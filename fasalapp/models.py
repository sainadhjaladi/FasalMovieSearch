from django.db import models

class User(models.Model):
    uname = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    uemail = models.EmailField()
    password = models.CharField(max_length=15)

    class Meta:
        db_table = "user"



class Playlist(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField()

    def __str__(self):
        return self.title
