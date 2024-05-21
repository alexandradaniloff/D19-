
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField

class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
    dd = 'ДД'
    tk = 'Танк'
    hl = 'Хил'
    tr = 'Торговец'
    gm = 'Гильдмастер'
    qg = 'Квестгивер'
    bs = 'Кузнец'
    tn = 'Кожевник'
    pm = 'Зельевар'
    sm = 'Мастер заклинаний'
    CATEGORY_TYPES = [
        (dd, 'DAMAGEDILLER'),
        (tk, 'TANK'),
        (hl, 'HEALER'),
        (tr, 'TRADER'),
        (gm, 'GILDMASTER'),
        (qg, 'QUESTGIVER'),
        (bs, 'BLACKSMITH'),
        (tn, 'TANNER'),
        (pm, 'POTIONMAKER'),
        (sm, 'SPELLMASTER'),
    ]
    name = models.CharField(max_length=17, choices=CATEGORY_TYPES)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def subscribe(self):
        pass

    def get_category(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    content = RichTextUploadingField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    post_updated_ad = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return f'{self.post_author} : {self.content}'

        # def preview(self):
        #     preview = f'{self.content[:50]}'
        #     return preview
        #
        # def get_absolute_url(self):
        #     return reverse('post_detail', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['post_created_at']

    def get_absolute_url(self):
        return reverse('post')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='PostComment')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'author', verbose_name="Автор")
    content = models.TextField(verbose_name="Описание")
    comment_created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name="Статус")

    def __str__(self):
        return f'{self.comment_author} : {self.content}'

    def priview(self):
        preview = f' {self.text[:124]}'
        return preview

    def get_absolute_url(self):
        return reverse('post')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['id']

