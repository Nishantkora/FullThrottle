# Generated by Django 2.2 on 2020-06-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200604_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50, verbose_name='User Name'),
            preserve_default=False,
        ),
    ]