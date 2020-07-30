# Generated by Django 2.2.14 on 2020-07-23 08:40

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('icon', models.ImageField(blank=True, max_length=200, null=True, upload_to='media/uploads/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True, verbose_name='电话')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_of', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]
