from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='название')
    text = models.TextField(verbose_name='текст статьи')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
