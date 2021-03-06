# Generated by Django 3.2 on 2021-05-01 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0008_post_public_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(max_length=225, unique=True)),
                ('comment', models.TextField(null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField()),
            ],
            options={
                'ordering': ['-createAt'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(default='c31dd36e-1906-452a-8a5c-90bfbabe9625', max_length=225, unique=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.comment')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='public_id',
            field=models.CharField(default='a4804a3e-c46d-47a9-bebe-3372948af035', max_length=225, unique=True),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.IntegerField(default=0)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('notifications', models.ManyToManyField(to='database.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(max_length=225, unique=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-createAt'],
            },
        ),
        migrations.AddField(
            model_name='group',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.likes'),
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(related_name='comment_many_to_many', to='database.Comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='like_many_to_many', to='database.Likes'),
        ),
    ]
