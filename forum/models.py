# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=E5142
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # profile_picture =

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(max_length=30)
    # users = models.ManyToManyField(User)
    # question = models.ManyToManyField(Question)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Question(models.Model):
    title = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=150)
    question = models.TextField()
    # answer = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    questioner = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    answered = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    # like_num = models.IntegerField()
    # report_num = models.IntegerField()

    def __str__(self):
        return self.title

    def categories(self):
        return ", ".join([str(c) for c in self.category.all()])

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    answerer = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    # like_num = models.IntegerField()
    # report_num = models.IntegerField()
    # approved = models.BooleanField(default=False)

    def __str__(self):
        return "Answer to:  <" + self.question.title + ">  by " + str(self.answerer)



    # def get_total_likes(self):
    #     return self.likes.users.count()


# class Like(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     users = models.ManyToManyField(User)
#     date_liked = models.DateTimeField(auto_now_add=True)
