from pydoc import describe
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _



class Article(models.Model):
    name  = models.CharField(_("نام و نام خانوادگی "), max_length=30)
    National_code = models.IntegerField(_("کد ملی "))
    date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    describtion = models.TextField(_("توضیحات "), blank=True)
    auther = models.ForeignKey(User, on_delete=models.PROTECT, default='admin') #    settings.AUTH_USER_MODEL
    tags = models.ManyToManyField("Tag", related_name="articles", blank=True, null=True)
    #   public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
class Tag(models.Model):
    title = models.CharField(_("عنوان "), max_length=100)
    slug = models.SlugField()
    date_tag = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_time_tag = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title



