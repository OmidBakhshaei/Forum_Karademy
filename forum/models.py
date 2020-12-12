# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=E5142
# pylint: disable=W0222
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(max_length=30, unique=True,)
    # users = models.ManyToManyField(User)
    # question = models.ManyToManyField(Question)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    question = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    questioner = models.ForeignKey(
        User, null=True ,on_delete=models.SET_NULL, related_name="questions"
    )
    answered = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name="categories")
    likes = models.ManyToManyField(User, blank=True, null=True, related_name="likes")
    reports = models.ManyToManyField(User, blank=True, null=True, related_name="reported_questions")

    def __str__(self):
        return self.title

    def topics(self):
        return ", ".join([str(c) for c in self.category.all()])

    def get_absolute_url(self):
        return reverse("question_details", args=(str(self.id)))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def get_total_likes(self):
        return self.likes.count()


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="questions", on_delete=models.CASCADE)
    answer = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    answerer = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True, null=True, related_name="liked_answers")
    approved = models.BooleanField(default=False)
    reports = models.ManyToManyField(User, blank=True, null=True, related_name="reported_answers")

    def __str__(self):
        return "Answer to:  <" + self.question.title + ">  by " + str(self.answerer)

    def get_total_likes(self):
        return self.likes.count()


# class Like(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     users = models.ManyToManyField(User)
#     date_liked = models.DateTimeField(auto_now_add=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()
    # profile_picture =
