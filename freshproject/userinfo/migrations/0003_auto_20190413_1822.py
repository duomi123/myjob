# Generated by Django 2.1.7 on 2019-04-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20190413_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='receiver',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(default='', max_length=40),
        ),
    ]