# Generated by Django 5.0.6 on 2024-05-20 22:14

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board_News', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ДД', 'DAMAGEDILLER'), ('Танк', 'TANK'), ('Хил', 'HEALER'), ('Торговец', 'TRADER'), ('Гильдмастер', 'GILDMASTER'), ('Квестгивер', 'QUESTGIVER'), ('Кузнец', 'BLACKSMITH'), ('Кожевник', 'TANNER'), ('Зельевар', 'POTIONMAKER'), ('Мастер заклинаний', 'SPELLMASTER')], max_length=17)),
                ('subscribers', models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('post_updated_ad', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board_News.category')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание')),
                ('comment_created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PostComment', to='Board_News.post')),
            ],
        ),
    ]
