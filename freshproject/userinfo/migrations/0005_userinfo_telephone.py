# Generated by Django 2.1.7 on 2019-04-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_userinfo_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='telephone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
