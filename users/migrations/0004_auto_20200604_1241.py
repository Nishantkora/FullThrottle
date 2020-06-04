# Generated by Django 2.2 on 2020-06-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200604_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='admin@throttle.com', max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]