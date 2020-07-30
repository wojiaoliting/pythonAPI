# Generated by Django 2.2.14 on 2020-07-24 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True, verbose_name='标题')),
                ('summary', models.CharField(blank=True, max_length=200, null=True, verbose_name='摘要')),
                ('body', models.TextField()),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('title_icon', models.ImageField(blank=True, max_length=200, null=True, upload_to='media/uploads/article/%Y/%m/%d/')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True, verbose_name='电话')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_from', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
    ]