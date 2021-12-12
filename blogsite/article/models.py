from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length = 100, verbose_name='Тема')
    body = models.TextField(verbose_name='Текст')
    def __str__(self):
        return self.title