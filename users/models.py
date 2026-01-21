from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    自定义用户模型
    继承 AbstractUser 后，我们自动拥有了 username, email, password 等字段
    我们可以在这里添加额外的字段，比如 'phone' 或 'role'
    """
    bio = models.TextField("个人简介", blank=True, null=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username