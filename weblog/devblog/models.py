from django.db import models

class Article(models.Model):
    article_id = models.IntegerField()
    title = models.CharField(max_length=150, default="NoTitle")
    preview = models.CharField(max_length=1500, default="NoPriview")
    text = models.CharField(max_length=10000, default="NoText")
    interest = models.CharField(max_length=35, default="Global")

class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    status = models.CharField(max_length=10)
    session_id = models.CharField(max_length=45, default="NoSessionId")
    interest1 = models.CharField(max_length=35, default="NoInterest")
    interest2 = models.CharField(max_length=35, default="NoInterest")
    interest3 = models.CharField(max_length=35, default="NoInterest")
    interest4 = models.CharField(max_length=35, default="NoInterest")
    interest5 = models.CharField(max_length=35, default="NoInterest")

class History(models.Model):
    article_id = models.IntegerField()
    title = models.CharField(max_length=150, default="NoTitle")
    preview = models.CharField(max_length=40, default="NoPriview")
    userProfile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=1)