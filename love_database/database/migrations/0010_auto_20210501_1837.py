# Generated by Django 3.2 on 2021-05-01 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0009_auto_20210501_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='public_id',
            field=models.CharField(default='888308a3-efc0-4258-83ec-a5025dfa6511', max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='public_id',
            field=models.CharField(default='17a08479-45a3-48e9-bb45-3f9f1695ee49', max_length=225, unique=True),
        ),
    ]
