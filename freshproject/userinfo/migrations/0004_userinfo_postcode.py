# Generated by Django 2.1.7 on 2019-04-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20190413_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='postcode',
            field=models.CharField(default='', max_length=6),
        ),
    ]